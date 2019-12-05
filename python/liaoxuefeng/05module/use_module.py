#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'a test module'

__author__ = 'haha'

import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print ('Hello world')
    elif len(args) == 2:
        print ('Hello, %s!' % args[1])
    else:
        print ('Too many arguments!')
    print(__doc__)

if __name__ == '__main__':
    test()

# sys模块的 argv变量，用 list存储了命令行的所有参数。
# argv至少有一个元素，因为 第一个参数永远是该 .py文件的名称

# 在命令行运行该模块文件时，解释器把一个特殊变量 __name__置为 __main__
# 如果是在其他地方导入该模块，if判断失败

'''
正常的函数和变量名是公开的，如 abc, 1234
特殊变量可以被直接引用，但有特殊用途，如 __author__, __name__
                                  __doc__可以访问模块定义的文档注释
非公开的函数和变量，不应该被直接引用，如 _xxx, __xxx
'''