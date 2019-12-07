# 判断对象类型
# 基本类型、一个变量指向函数或者类，可以用 type()
strType = type('123')
print (strType)

type(123) == type(456)
type(789) == int
type('123') == str

# 判断一个对象是否是函数
# 使用 types模块中定义的常量
import types
def fn():
    pass

a = type(fn) == types.FunctionType
b = type(abs) == types.BuiltinFunctionType
c = type(lambda x : x) == types.LambdaType
d = type((x for x in range(10))) == types.GeneratorType

print (a, b, c, d)

# 判断 class类型，由于继承关系的存在，可以使用 isinstance()
# 能用 type()判断的基本类型也可以用 isinstance()
class Animal(object):
    pass

class Dog(Animal):
    pass

dog = Dog()
e = isinstance(dog, Animal)
f = isinstance(dog, Dog)

print (e, f)


# 使用 dir()
# 要获取一个对象的所有属性和方法，可以使用 dir()
Alpha = 'ABC'
g = dir(Alpha)
h = len(Alpha) == Alpha.__len__()
print (h)

# 配合 getattr()、setattr()、hasattr()，可以直接操作一个对象的状态
class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x

obj = MyObject()

i = hasattr(obj, 'x')
j = hasattr(obj, 'y')
k = setattr(obj, 'y', 19)
l = hasattr(obj, 'y')
m = getattr(obj, 'y')
n = obj.y
# 传一个 default参数，如果属性不存在，返回默认值
o = getattr(obj, 'z', 404)
# 获取对象的方法
p = hasattr(obj, 'power')
q = getattr(obj, 'power')
q()
print (i, j, k, l, m, n, o, p, q, q(), sep = '\n')

