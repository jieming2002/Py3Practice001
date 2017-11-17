__author__ = 'skye2017-11-15'
# coding: utf-8
import  keyword

# 此项目练习 Python 3 教程 http://www.runoob.com/python3/python3-data-type.html
print('hello world')
print('你好，中国')

# Python 的标准库提供了一个 keyword 模块，可以输出当前版本的所有关键字：
print(keyword.kwlist)

# python最具特色的就是使用缩进来表示代码块，不需要使用大括号
if True:
    print('true')
else:
    print('false')

if True:
    print('answer')
    print('true')
else:
    print('answer')
  #   缩进数的空格数不一致，会导致运行错误：
  # print('false') IndentationError: unindent does not match any outer indentation level

# Python 通常是一行写完一条语句，但如果语句很长，我们可以使用反斜杠(\)来实现多行语句
item1 = 'item1'
item2 = 'item2'
item3 = 'item3'
total = item1 + ' ' + \
    item2 + ' ' + \
    item3;
print('total = '+total)

# 在 [], {}, 或 () 中的多行语句，不需要使用反斜杠(\)
total = ['item1', 'item2',
         'item3', 'item4',
         'item5']
print('total = {0}'.format(total))

# 字符串
# python中单引号和双引号使用完全相同。
# 使用三引号('''或""")可以指定一个多行字符串。
"""
自然字符串， 通过在字符串前加r或R。 如 r"this is a line with \n" 则\n会显示，并不是换行。
python允许处理unicode字符串，加前缀u或U， 如 u"this is an unicode string"。
字符串是不可变的。
"""
s = 'this is a line with \n do you know? 是的'
print('s = '+s)
s = r'this is a line with \n do you know?'
print('s = '+s)
s = u'this is a line with \n do you know?'
print('s = '+s)

'''空行
函数之间或类的方法之间用空行分隔
空行与代码缩进不同，空行并不是Python语法的一部分。书写时不插入空行，Python解释器运行也不会出错。
空行的作用在于分隔两段不同功能或含义的代码，便于日后代码的维护或重构。
记住：空行也是程序代码的一部分。
'''

# 等待用户输入
input('\n\n请输入内容，按 enter 键退出。')

# Python 可以在同一行中使用多条语句，语句之间使用分号(;)分隔
x = 1; y = 2; print('x + y = {0}'.format(x + y))

'''多个语句构成代码组
缩进相同的一组语句构成一个代码块，我们称之代码组。
像if、while、def和class这样的复合语句，首行以关键字开始，以冒号结束，该行之后的一行或多行代码构成代码组
我们将首行及后面的代码组称为一个子句(clause)
'''
if False:
    print('false')
    print('is')
elif x == 1:
    print('x = '+str(x))
else:
    print('最后这里')

# print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=""：
print('第一行')
print('第二行', end='')
print('第三行')

'''import 与 from...import
将整个模块(somemodule)导入，格式为： import somemodule
从某个模块中导入某个函数,格式为： from somemodule import somefunction
从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
将某个模块中的全部函数导入，格式为： from somemodule import *
'''
import sys
print('命令行参数为:')
for i in sys.argv:
    print(i)
print('\n python 路径为',sys.path)

from sys import argv,path  #  导入特定的成员
print('path:',path) # 因为已经导入path成员，所以此处引用时不需要加sys.path

# 调用 python 的 help() 函数可以打印输出一个函数的文档字符串：
help(max)
