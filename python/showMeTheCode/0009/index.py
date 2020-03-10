# 一个HTML文件，找出里面的链接
import requests
from bs4 import BeautifulSoup

def get_links(html):
    soup = BeautifulSoup(html, features='lxml')
    links = []
    for link in soup.find_all('a'):
        href = link['href']
        if href.startswith('http'):
            links.append(href)
    return links

if __name__ == '__main__':
    r = requests.get('https://github.com/')
    html = r.text
    links = get_links(html)
    print (links)
