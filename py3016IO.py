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

# 这里有两种方式输出一个平方与立方的表:
for x in range(1,11):
    # 这个例子展示了字符串对象的 rjust() 方法, 它可以将字符串靠右, 并在左边填充空格。
    print(repr(x).rjust(3), repr(x**2).rjust(4), repr(x**3).rjust(5))

for x in range(1,11):
    # 还有类似的方法, 如 ljust() 和 center()
    print(repr(x).ljust(3), repr(x**2).ljust(4), repr(x**3).ljust(5))
    # 另一个方法 zfill(), 它会在数字的左边填充 0

for x in range(1,11):
    # 还有类似的方法, 如 ljust() 和 center()
    print(repr(x).center(3), repr(x**2).center(4), repr(x**3).center(5))

for x in range(1,11):
    print('{0:3d} {1:4d} {2:5d}'.format(x, x**2, x**3))




