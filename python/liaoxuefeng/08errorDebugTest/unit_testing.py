# 测试驱动开发（TDD: Test-Driven Development）
# 单元测试是用来对一个模块，一个函数或一个类来进行正确性检验的测试工作

class Dict(dict):

    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

# 编写单元测试，引入 unittest模块
import unittest

# 编写一个从 unittest.TestCase继承的类
# 以 test函数开头的方法都是测试方法，不以 test开头不会被认为是一个测试方法，测试的时候不执行
class UnitTesting(unittest.TestCase):

    # setUp和 tearDown会在每调用一个测试方法的前后分别被执行
    def setUp(self):
        print ('setUp...')

    def tearDown(self):
        print ('tearDown...')

    def test_init(self):
        d = Dict(a = 1, b = 'test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertEqual(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(key):
        d = Dict()
        with self.assertRaises(KeyError):
            value = q['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

# 运行单元测试
# 第一种方式
if __name__ == '__main__':
    unittest.main()

# 第二种方式
# 推荐做法
# python -m unittest xx.py



