# 定义一个 class，可以从某个现有的 class继承，新的 class称为 子类(Subclass)
# 被继承的 class称为基类、父类或超类（Bass class、Super class）

class Animal(object):
    def run(self):
        print ('Animal is running...')

# Dog类继承 Animal类
class Dog(Animal):
    def run(self):
        print ('Dog is running...')

    def eat(self):
        print ('Eating...')

# Cat类继承 Animal类
class Cat(Animal):
    def run(self):
        print ('Cat is running...')

class Tortoise(Animal):
    def run(self):
        print ('Tortoise is running slowly')

# 子类和基类存在相同的方法时，子类的方法会覆盖基类的方法，总是会调用子类的 方法，这就是继承的好处：多态
dog = Dog()
dog.run()

cat = Cat()
cat.run()

print (isinstance(dog, Animal))
print (isinstance(dog, Dog))


# 多态
# 多态的好处，传入的子类，都有基类的方法，不在意子类的类型
def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal())
run_twice(Dog())
run_twice(Cat())
run_twice(Tortoise())

# 开闭原则
# 对拓展开放：允许新增 Animal子类
# 对修改封闭：不需要修改依赖 Animal类型的 run_twice()等函数

'''
静态语言 vs动态语言

静态语言：需要传入 Animal类型，那传入的对象必须是 Animal类型或者它的子类，否则无法调用 run()方法
动态语言：不一定需要传入 Animal类型，只需要保证传入的对象有一个 run()方法

这就是动态语言的 ’鸭子类型‘，开起来像鸭子，走路像鸭子，它就可以看做是鸭子

Python的 file-like object就是一种鸭子类型
'''

