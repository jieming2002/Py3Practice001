__author__ = 'skye2017-11-19'
# coding=utf-8
import math

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

# 如果在 format() 中使用了关键字参数, 那么它们的值会指向使用该名字的参数。
print('姓名：{name}，专业：{site}'.format(name='盛开', site='人工智能工程师特训班'))

# 位置及关键字参数可以任意的结合:
print('学生姓名：{1}、{leader}、{0}'.format('小明', '小张', leader='小唐'))

# '!a' (使用 ascii()), '!s' (使用 str()) 和 '!r' (使用 repr()) 可以用于在格式化某个值之前对其进行转化:
print('常量 PI 的值近似为：{}'.format(math.pi))
print('常量 PI 的值近似为：{!a}'.format(math.pi))
print('常量 PI 的值近似为：{!s}'.format(math.pi))
print('常量 PI 的值近似为：{!r}'.format(math.pi))
a = '0X'
print('常量 PI 的值近似为：{!a}'.format(a))
print('常量 PI 的值近似为：{!s}'.format(a))
print('常量 PI 的值近似为：{!r}'.format(a))

# 可选项 ':' 和格式标识符可以跟着字段名。下面的例子将 Pi 保留到小数点后三位：
print('常量 PI 的值近似为：{0:.3F}'.format(math.pi))

# 在 ':' 后传入一个整数, 可以保证该域至少有这么多的宽度。
table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
for name, val in table.items():
    print('{0:10} = {1:5d}'.format(name, val))

# 如果你有一个很长的格式化字符串, 而你不想将它们分开, 那么在格式化时通过变量名而非位置会是很好的事情。
# 最简单的就是传入一个字典, 然后使用方括号 '[]' 来访问键值 :
print('Runoob:{0[Runoob]:d}; Google:{0[Google]:d}; Taobao:{0[Taobao]:d}'.format(table))
# 也可以通过在 table 变量前使用 '**' 来实现相同的功能：
print('Runoob:{Runoob:d}; Google:{Google:d}; Taobao:{Taobao:d}'.format(**table))

# 旧式字符串格式化 %
# str.format() 比较新的函数
# 大多数 Python 代码仍然使用 % 操作符。但是因为这种旧式的格式化最终会从该语言中移除, 应该更多的使用 str.format().









