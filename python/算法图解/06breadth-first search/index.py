'''
广度优先搜索（breadth-first search, BFS）
图算法的一种，能找到两样东西之间的最短距离

图
有向图（directed graph），其中关系是单向的
无向图（undirected graph）没有箭头，直接相连的节点互为邻居

队列
队列是先进先出（first in first out, FIFO）的数据结构
栈是后进先出（last in first out, LIFO）的数据结构
'''
from collections import deque

# 创建图
graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []

def personIsSeller(name):
    return name[-1] == 'm'

def search(name):
    # 创建队列
    searchQueue = deque()
    searchQueue += graph[name]
    # 搜索过的不再搜索
    searched = []

    while searchQueue:
        person = searchQueue.popleft()
        if not person in searched:
            if personIsSeller(person):
                print (person + ' is a mango seller')
                return True
            else:
                searchQueue += graph[person]
                searched.append(person)
    return False

search('you')
