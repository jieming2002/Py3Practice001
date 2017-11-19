__author__ = 'skye2017-11-19'
# coding=utf-8

'''模块是一个包含所有你定义的函数和变量的文件，其后缀名是.py
模块可以被别的程序引入，以使用该模块中的函数等功能。
一个模块只会被导入一次，不管你执行了多少次 import
Python的搜索路径被存储在 sys 模块中的 path 变量
可以在脚本中修改 sys.path 来引入一些不在搜索路径中的模块。
'''
import sys
print(sys.path)

import fibo
# 如果你打算经常使用一个函数，你可以把它赋给一个本地的名称：
fib = fibo.fib
fib(11)

# 模块除了方法定义，还可以包括可执行的代码。这些代码一般用来初始化这个模块。这些代码只有在第一次被导入时才会被执行。
# 关键在于被导入时，会执行里面的代码。
from fibo import fib, fib2
# 这种导入的方法不会把被导入的模块的名称放在当前的字符表中

'''一个模块被另一个程序第一次引入时，其主程序将运行。
如果我们想在模块被引入时，模块中的某一程序块不执行，
我们可以用 __name__ 属性来使该程序块仅在该模块自身运行时执行。
'''

# 内置的函数 dir() 可以找到模块内定义的所有名称。以一个字符串列表的形式返回:
print(dir(fibo))
# 如果没有给定参数，那么 dir() 函数会罗列出当前定义的所有名称:

# 目录只有包含一个叫做 __init__.py 的文件才会被认作是一个包
# 导入语句遵循如下规则：
# 如果包定义文件 __init__.py 存在一个叫做 __all__ 的列表变量，那么在使用 from package import * 的时候就把这个列表中的所有名字作为包内容导入。
# 作为包的作者，可别忘了在更新包之后保证 __all__ 也更新
# 如果 __all__ 真的没有定义，那么使用from sound.effects import *这种语法的时候，就不会导入包 sound.effects 里的任何子模块。
# 他只是把包sound.effects和它里面定义的所有内容导入进来
# 通常我们并不主张使用*这种方法来导入模块，因为这种方法经常会导致代码的可读性降低。
# 记住，使用from Package import specific_submodule这种方法永远不会有错。事实上，这也是推荐的方法。
