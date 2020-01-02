# 在程序运行时，所有的变量都在内存中
# 变量从内存中变成可储存或传输的过程称之为 序列化，python中称为 picking
# 序列化之后，把序列化后的内容写入磁盘或者传输到其他机器
# 把变量内容从序列化后的对象重新读到内存里称为 反序列化，unpicking

# pickle模块实现序列化
import pickle, os
absPh = os.path.abspath('.')
testFilePath = os.path.join(absPh, 'test.py')
d = dict(name = 'Bob', age = 20, score = 88)

byContent = pickle.dumps(d)
# print (byContent)
# pickle.dumps() 把任意对象序列化成一个 bytes
# pickle.dump() 把对象序列化后写入一个 file-like Object
f = open(testFilePath, 'wb')
pickle.dump(d, f)
f.close()

f = open(testFilePath, 'rb')
# pickle.loads() 方法反序列出对象
# pickle.load() 从一个 file-like Object中反序列出对象
newD = pickle.load(f)
f.close()
# print (newD)


# JSON
# 要在不同编程语言之间传递对象，必须把对象序列化为标准格式
# JSON可以被所有语言读取，也方便存储到磁盘或网络传输，JSON编码为 utf-8
'''
JSON类型      Python类型
{}              dict
[]              list
"string"        str
123.45          int或 float
true/false      True/False
null            None
'''

# json模块提供了 python对象到JSON的相互转换
import json
jsonContent = json.dumps(d)
# dumps() 方法返回一个 str
# dump() 把 JSON写入一个 file-like Object
print (jsonContent)

# loads() 将 JSON字符串反序列化
# load() 从 file-like Object中读取字符串并反序列化
jsonDict = json.loads(jsonContent)
print (jsonDict)

# 将 class序列化为 JSON
# 为 dumps传入一个转换函数
# 将 class的实例变成 dict
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Bob', 20, 88)

def student2Dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }

dictStudent = json.dumps(s, default = student2Dict)
print (dictStudent)
# 只对当前 class有效

# 每个实例都有一个__dict__属性，是 dict，用于存储实例变量，定义 __slots__的例外
jsonStudent = json.dumps(s, default = lambda obj : obj.__dict__)
print (jsonStudent)

# 反序列化
def dict2Student(d):
    return Student(d['name'], d['age'], d['score'])

originClass = json.loads(jsonStudent, object_hook=dict2Student)
print (originClass)




















































