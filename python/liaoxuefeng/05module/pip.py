'''
在 Python中，安装第三方模块，是通过包管理工具 pip完成的
第三方库都会在 Python官方的 pypl.python.org网站注册

模块搜索路径：
加载一个模块的时候，Python解释器会按照
当前目录、所有已安装的内置模块、第三方模块的顺序进行搜索
搜索路径会放在 sys模块的 path变量中
'''

import sys
print (sys.path)

# 添加自己的搜索目录
# 一是直接修改 sys.path，添加要搜索的目录
sys.path.append('/Users/michael/my_py_scripts')
# 该方法会在运行时修改，运行结束后失效

# 二是设置环境变量 PYTHONPATH，该环境变量的内容会被自动添加到模块搜索路径中