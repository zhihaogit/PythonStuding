# 动态语言和静态语言最大不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的
class Hello(object):
    def hello(self, name = 'world'):
        print ('Hello, %s.' % name)

# 当解释器载入 hello模块时，就会依次执行该模块的所有语句，执行结果就是动态创建一个 Hello的 class对象

h = Hello()
# type()
# 可以查看一个类型或变量德类型，Hello是一个 class，他的类型就是 type，而 h是一个实例，它的类型就是 class Hello
# 创建 class的方法就是使用 type()函数
# type()函数既可以返回一个对象的类型，又可以创建出新的类型
def fn(self, name = 'world'):
    print ('Hello, %s.' % name)

# 创建 Hello class
Hello = type('Hello', (object,), dict(hello = fn))
h = Hello()
print (h.hello())
print (type(Hello))
print (type(h))
# 创建一个class对象，type()需要3个参数
# 1. class的名称
# 2. 继承的父类集合，python支持多重继承，只有一个父类，使用 tuple的单元素写法
# 3. class的方法名称与函数绑定

# python解释器遇到 class定义式，回扫描 class写法，然后调用 type()函数创建 class



# metaclass
# 先定义 metaclass，就可以创建类，最后创建实例
# metaclass允许创建类或者修改类，可以把类当做是 metaclass创建出来的实例
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

class MyList(list, metaclass = ListMetaclass):
    pass
# 传入关键字参数 metaclass之后，它会指示解释器在创建 MyList时，要通过 ListMetaClass.__new__()来创建，可以在这个时候修改类的定义
# __new__()，接收的参数依次是：
# 1. 当前准备创建的类的对象
# 2. 类的名字
# 3. 类继承的父类集合
# 4. 类的方法集合

L = MyList()
L.add(2)
print (L)
# 普通的 list没有 add方法
L2 = list()
# L2.add(1)

