# class中有很多特殊用途的函数，可以帮助进行定制类
class Student(object):
    def __init__(self, name):
        self.name = name

    # 为了打印的更清晰，可以使用 __str__方法
    def __str__(self):
        return 'Student object (name: %s)' % self.name

    # 直接敲变量，不用 print()，打印出来依旧不好看
    # 直接显示变量调用的不是 __str__()，而是 __repr__()
    # __str__返回用户看到的字符串，__repr__返回开发人员看到的字符串，为调试服务的
    __repr__ = __str__

s = Student('Bob')
# print (s)


# 如果一个类想被 for...in...循环，就必须实现一个 __iter__()方法
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:
            raise StopIteration()
        return self.a

    # 像 list一样用下标取出元素，使用 getitem()方法
    # 模仿 list的切片方法
    # __setitem__()方法，__delitem__()方法
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a 
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

f = Fib()
# for n in f:
#     print (n)
fInt = f[5]
fSlice = f[: 10]
# print (fSlice)


# __getattr__
# 当调用不存在的属性时，解释器会试图调用 __getattr__(self, property)来尝试获取属性
# 可以返回值和函数
class StudentTest(object):

    def __init__(self):
        self.name = 'hahaha'

    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        if attr == 'age':
            return lambda : 25
        # 让 class只响应特定几个属性，其他的会返回 None，可按照约定，抛出 AttributeError错误
        return AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

st = StudentTest()
print (st.name, st.age(), st.x)

# 这实际是把一个类的所有属性和方法调用全部动态化处理了
class Chain(object):

    def __init__(self, path = ''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

p1 = Chain().status.user.timeline.list
print (p1)

# __call__
# 任何类，只需要定义一个 __call__()方法，就可以直接对实例进行调用
# 还可以定义参数
class StudentTest2(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print ('My name is %s.' % self.name)

st2 = StudentTest2('jjj')
st2()

# Callable
# 判断一个对象能否被调用
scr = callable(Student('ada'))
scr2 = callable(StudentTest2('dfa'))
print (scr, scr2)







