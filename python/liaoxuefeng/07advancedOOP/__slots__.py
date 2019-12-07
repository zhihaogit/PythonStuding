# 定义一个class，创建一个实例之后，可以给该实例绑定任何属性和方法
class Student(object):
    pass

s = Student()
# 给实例绑定一个属性
s.name = 'Michael'
print (s.name)
# 给实例绑定一个方法
def set_age(self, age):
    self.age = age

# s.set_age = set_age
from types import MethodType
s.set_age = MethodType(set_age, s)

s.set_age(123)
print (s.age)

# 给一个实例绑定的方法，对另一个实例不起作用
# 为了而给所有实例绑定方法，可以给 class绑定方法
def set_socre(self, score):
    self.score = score

Student.set_socre = set_socre

s.set_socre(100)
print (s.score)


# 使用 __slots__限制该 class实例能添加的属性

class StudentTest(object):
    __slots__ = ('name', 'age')

sTest = StudentTest()
sTest.name = 'Michael'
sTest.age = 12
# sTest.score = 123
sTest.set_socre = MethodType(set_socre, sTest)
sTest.set_socre = set_socre
# sTest.set_socre(123)
print (sTest.set_socre)

# __slot__的限制只对当前类实例起作用，对继承的子类不起作用
class GraduateStudent(Student):
    pass

g = GraduateStudent()
g.score = 999

# 除非在子类中定义 __slots__，这样，子类实例允许定义的属性就是自身的 __slots__加上基类的 __slots__
