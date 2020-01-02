# 通过特殊的 __init__方法，在创建实例的时候，把name，score等属性绑上去
class Student(object):

    # __init__方法的第一个参数永远是 self，表示创建的实例本身
    # 在__init__方法内部，就可以把各种属性绑定到 self上，因为 self指向创建的实例本身
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

bart = Student('fa', 12);
# 可以自由地给一个实例变量绑定属性
bart.age = 123
bart.grade = bart.get_grade()

print (bart.grade)

'''
类是创建实例的模板，而实例则是一个一个具体的对象，各个实例拥有的数据互相独立
方法是与实例绑定的函数，和普通函数不同，方法可以直接访问实例的数据
通过在实例上调用方法，可以直接操作对象内部的数据，并且无需知道方法内部的实现细节
和静态语言不同，Python允许对实例变量绑定任何数据
'''