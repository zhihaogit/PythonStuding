# 枚举类 enumerate
# 使用枚举类型定义一个 class类型，然后每个常量都是 class的一个唯一实例
# 使用 Enum类来实现这个功能
from enum import Enum, unique

monthName = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
Month = Enum('Month', monthName)

# 引用常量
print (Month.Jan)
# 枚举所有成员
for name, member in Month.__members__.items():
    print (name, '=>', member, ',', member.value)
# value属性时自动赋给成员的 int常量，默认从 1计数

# @unique装饰器帮助检查保证没有重复值
@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

day1 = Weekday.Mon
day2 = Weekday.Tue.value
print (day1, day2)

# @unique
# class Gender(Enum):
#     Male = 0
#     Female = 1
Gender = Enum('Gender', ('Male', 'Female'))

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

# 测试:
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')

# Enum可以把一组相关常量定义在一个 class中，且 class不可变，而且成员可以直接比较
