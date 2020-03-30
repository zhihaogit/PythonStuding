# 贪婪算法（greedy algorithm）
# 每步都采取最优的做法 -> 局部最优解带来全局最最优解

# 近似算法
# 广播台覆盖问题
# 需要覆盖的元素集合
states_needed = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])
# 可供选择的广播台清单
stations = {}
stations['kone'] = set(['id', 'nv', 'ut'])
stations['ktwo'] = set(['wa', 'id', 'mt'])
stations['kthree'] = set(['or', 'nv', 'ca'])
stations['kfour'] = set(['nv', 'ut'])
stations['kfive'] = set(['ca', 'az'])
# 最终选择的广播台
final_stations = set()

while states_needed:
    best = None
    states_covered = set()
    for station, states in stations.items():
        covered = states_needed & states
        if len(covered) > len(states_covered):
            best = station
            states_covered = covered
    states_needed -= states_covered
    final_stations.add(best)

print (final_stations)

'''
NP完全问题
元素较少时算法的运行速度非常快，但随着元素数量的增加，速度会变得非常慢
涉及 所有组合的问题通常是 NP完全问题
不能将问题分成小问题，必须考虑各种可能的情况，这可能是 NP完全问题
如果问题涉及序列（如旅行商问题中的城市序列）且难以解决，这可能是 NP完全问题
如果问题涉及集合（如广播台集合）且难以解决，这可能是 NP完全问题
如果问题可转换为集合覆盖问题或旅行商问题，那肯定是 NP完全问题

小结
贪婪算法寻找局部最优解，企图以这种方式获得全局最优解
对于 NP完全问题，还没有找到快速解决方案
面临 NP完全问题，最佳的做法是使用 近似算法
贪婪算法易于实现、运行速度快，是不错的近似算法
'''