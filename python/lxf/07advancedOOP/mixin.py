# 继承是面向对象编程的一个重要的方式，因为通过继承，子类就可以拓展父类的功能
# 多重继承
class Animal(object):
    pass

# 大类
class Mammal(Animal):
    pass

class Bird(Animal):
    pass

# 动物
class Dog(Mammal):
    pass

class Bat(Mammal):
    pass

class Parrot(Bird):
    pass

class Ostrich(Bird):
    pass

# 功能
class RunnableMixIn(object):
    def run(self):
        print ('Running...')

class Flyable(object):
    def fly(self):
        print ('Flying...')

class CarnivorouMixIn(Animal):
    def eat(self):
        print ('Eating meat...')


# 对于需要 Runnable功能的动物，就多继承一个 Runnable
class Dog(Mammal, Runnable):
    pass

# 对于需要 Flyable功能的动物，就多继承一个 Flyable
class Bat(Mammal, Flyable):
    pass

# 通过多重继承，一个子类就可以同时获得多个父类的所有功能

# Mixin
# 在设计类的继承关系时，通常，主线都是单一继承下来
# 如果需要“混入”额外的功能，通过多重继承后就可以实现，同时继承几个类，这种设计通常称为 Minxin
class Dog(Mammal, RunnableMixIn, CarnivorouMixIn):
    pass

# Mixin的目的就是给一个类增加多个功能
# 不需要复杂而庞大的继承链，只要选择组合不同的类的功能，就可以快速构造出所需的子类
# 只允许的单一继承的语言（Java）不能使用 Mixin的设计