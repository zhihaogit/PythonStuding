# 根据类创建的实例可以任意绑定属性
# 给实例绑定属性的方法是通过实例变量，或者通过 self变量
class Student(object):
    """docstring for Student"""
    name = 'Student'
    def __init__(self, name):
        self.name = name

s = Student('Bob')
s.score = 90

print (s.name)
print (Student.name)
s.name = 'Michael'
print (s.name)
print (Student.name)
# 删除 实例的 name属性，会显示类的 name属性
del s.name
print (s.name) 


class StudentTest(object):
    """docstring for StudentTest"""
    count = 0
    def __init__(self, arg):
        StudentTest.count += 1
        self.arg = arg

# 测试用例
if StudentTest.count != 0:
    print('测试失败!')
else:
    bart = StudentTest('Bart')
    if StudentTest.count != 1:
        print('测试失败!')
    else:
        lisa = StudentTest('Bart')
        if StudentTest.count != 2:
            print('测试失败!')
        else:
            print('StudentTests:', StudentTest.count)
            print('测试通过!')

