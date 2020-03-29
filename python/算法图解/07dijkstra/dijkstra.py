'''
狄克斯特拉算法（Dijkstra）
处理加权图，找到权重最低的路径
只适用于 有向无环图（directed acyclic graph, DAG）
找出图中最便宜的节点，并确保没有得到该节点的更便宜的路径
不能讲狄克斯特拉算法用于包含负权边的图，可以用 贝尔曼-福德算法（Bellman-Ford algorithm）

步骤
1. 找出最便宜的节点，即可在最短时间内前往的节点
2. 对于该节点的邻居，检查是否有前往它们的更短路径，如果有，就更新其开销
3. 重复这个过程，直到对图中的每个节点都这样做了
4. 计算最终路径

狄克斯特拉算法用于每条边都有关联数字的图，这些数字称为 权重（weight）
带权重的图称为加权图（weighted graph）-> 狄克斯特拉算法适用于找加权图的最短路径
不带权重的图称为非加权图（unweighted graph）-> 广度优先搜索适用于找非加权图的最短路径
'''
# graph散列表
graph = {}
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2

graph['a'] = {}
graph['a']['fin'] = 1

graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5

graph['fin'] = {}

# costs散列表
infinity = float('inf')
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity

# parents散列表
parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None

# 记录已处理过的节点
processed = []
print (costs)
for node in costs:
    print (node)

def findLowestCostNode(costs):
    lowestCost = float('inf')
    lowestCostNode = None
    for node in costs:
        cost = costs[node]
        if cost < lowestCost and node not in processed:
            lowestCost = cost
            lowestCostNode = node
    return lowestCostNode

node = findLowestCostNode(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors:
        newCost = cost + neighbors[n]
        if costs[n] > newCost:
            costs[n] = newCost
            parents[n] = node
    processed.append(node)
    node = findLowestCostNode(costs)
print (costs, parents)
