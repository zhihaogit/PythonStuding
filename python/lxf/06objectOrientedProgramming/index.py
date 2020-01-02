# 面向对象编程 -- Object Oriented Programming, -> OOP
# 自定义的对象数据类型就是面试对象中的类（Class）的概念

std1 = {
    'name': 'Michael',
    'score': 98
}

std2 = {
    'name': 'Bob',
    'score': 81
}

def print_score(std):
    print ('%s: %s' % (std['name'], std['score']))

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print ('%s: %s' % (self.name, self.score))

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)

bart.print_score()
lisa.print_score()

'''
Class是一种抽象概念
面向对象的设计思想是抽象出 Class，根据 Class创建 instance
面向对象的抽象程度要比函数高，因为一个 Class既包含数据，又包含操作数据的方法
数据封装、继承和多态是面向对象的三大特点
'''