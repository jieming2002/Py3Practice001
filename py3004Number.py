__author__ = 'skye2017-11-16'
# coding=utf-8

# 数据类型是不允许改变的,这就意味着如果改变数字数据类型得值，将重新分配内存空间。
a = 1
print('a 的内存地址 = {0}'.format(id(a)))
a = 2
print('a 的内存地址 = {0}'.format(id(a)))

# 可以使用del语句删除一些数字对象的引用。
del a
# print('a 的内存地址 = {0}'.format(id(a))) NameError: name 'a' is not defined

# Python3 整型是没有限制大小的，可以当作 Long 类型使用，所以 Python3 没有 Python2 的 Long 类型。
# 注意：在不同的机器上浮点运算的结果可能会不一样。
# 变量在使用前必须先"定义"（即赋予变量一个值），否则会出现错误：

a = -2
print('a = {0}'.format(a))
print('abs(a) = {0}'.format(abs(a)))
print('pow(2,3) = {0}'.format(pow(2,3)))

# 随机数函数
a = range(10)
print('a = {0}'.format(a))

# 好多函数都没有
