class Student(object):

    def __init__(self, name, score):
        # 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__
        # 在 Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
        self.__name = name
        self.__score = score
        # 这样无法从外部访问 实例变量.__name和 实例变量.__score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

bart = Student('Bart Simpson', 59)

print (bart.get_score())

# 双下划线的变量不能直接从外部访问，是因为 Python解释器对外把 __name变量改成了 __Student__name
# 不同版本的解释器可能会把 __name改成不同的变量名


class Student2(object):
    genderRight = ['male', 'female']

    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):

        if gender in Student2.genderRight:
            self.__gender = gender
        else:
            raise ValueError('Gender value error')

studentA = Student2('haha', 'j')

print (studentA.get_gender())

studentA.set_gender('male')

print (studentA.get_gender())

