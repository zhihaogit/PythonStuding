class Student(object):
    """docstring for Student"""
    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an interger!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100')
        self._score = value
# 检查参数，在 set_score()
# 对任意 Student实例进行操作，不能再随心所欲的设计了

s = Student()
# s.set_score(60)
# sScore = s.get_score()
# print (sScore)


# 使用 @property装饰器是负责把一个方法变成属性调用
class StudentTest(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an interger')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100')
        self._score = value

# 加上 @property，先把一个 getter方法变成属性
# 此时 @property会创建另一个装饰器 @score.setter，负责把一个 setter方法变成属性赋值

st = StudentTest()
st.score = 60

print (st.score)

# 首先这个属性很可能是不能直接暴露的，而是通过 getter和 setter方法来实现的
# 还可以定义只读属性，只定义 getter方法，不定义 setter方法
class StudentTest2(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2019 - self._birth
# birth是可读写属性
# age是一个只读属性



class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self._width * self._height
    
# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!') 











    

        