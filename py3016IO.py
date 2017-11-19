__author__ = 'skye2017-11-19'
# coding=utf-8

'''如果你希望将输出的值转成字符串，可以使用 repr() 或 str() 函数来实现。
str()： 函数返回一个用户易读的表达形式。
repr()： 产生一个解释器易读的表达形式。
'''
s = '北京，欢迎你'
print(s)
print(str(s))
print(repr(s))

a = 1/7
print(a)
print(str(a))
print(repr(a))

x = 10 * 3.25
y = 200 * 200
s = 'x 的值为： ' + repr(x) + ',  y 的值为：' + repr(y) + '...'
print(s)

#  repr() 函数可以转义字符串中的特殊字符
hello = 'hello,\n 年轻人'
print(hello)
hellos = repr(hello)
print(hellos)

# repr() 的参数可以是 Python 的任何对象
s = repr((x, y, ('Google', 'Runoob')))
print(s)



