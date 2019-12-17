# collections是 内建的集合模块，提供了许多有用的集合类

# namedtuple
# namedtuple是一个函数，它用来创建一个自定义的 tuple对象，并且规定了元素的个数，并可以用属性而不是索引来引用 tuple的每个元素
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print (p.x, p.y)

isPoint = isinstance(p, Point)
isTuple = isinstance(p, tuple)
print (isPoint, isTuple)

Circle = namedtuple('Circle', ['x', 'y', 'r'])


# deque
# list是线性存储，索引访问元素很快，插入和删除元素效率低
# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
# 支持 append(), pop(), appendleft(), popleft()
from collections import deque
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print (q)


# defaultdict
# key不存在的时候，返回一个默认值
from collections import defaultdict
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print (dd['key1'], dd['key2'])


# OrderedDict
# 实现保持 key顺序的 dict
from collections import OrderedDict
# 无序的 key
d = dict([('a', 1), ('b', 2), ('c', 3)])
print (d, d.keys())
# 有序的 key
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])

print (od, od.keys())

# 实现 FIFO（先进先出）的 dict，超出容量限制，先删除最早添加的 key
from collections import OrderedDict

class LastUpdatedOrderedDict(OrderedDict):
    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last = False)
            print ('remove', last)
        if containsKey:
            del self[key]
            print ('set:', (key, value))
        else:
            print ('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)


# ChainMap
# 把一组 dict串起来并组成一个逻辑上的 dict，chainMap本身是一个 dict，但是查找的时候，会按照顺序在内部 dict依次查找
# eg: 应用程序往往都需要传入参数，参数可以通过命令行传入，可以通过环境变量传入，还可以有默认参数
# ChainMap实现参数的优先级，即先查命令行参数，如果没传入，再查环境变量，如果没有，就是用默认参数
from collections import ChainMap
import os, argparse

# 构造缺省参数
defaults = {
    'color': 'red',
    'user': 'guest'
}

# 构造命令行参数
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()
command_line_args = { k: v for k, v in vars(namespace).items() if v }

# 组合成 chainMap
combined = ChainMap(command_line_args, os.environ, defaults)

# 打印参数
print ('color=%s' % combined['color'])
print ('user=%s' % combined['user'])


# Counter
# 简单的计数器
# 统计字符出现的个数
from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1

print (c)



















