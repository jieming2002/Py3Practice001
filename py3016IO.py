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

# 打开一个文件 'w' 只用于写 (如果存在同名文件则将被删除),
f = open('./data/test.txt', 'w')
f.write('Python 是一个非常好的语言。\n是的，的确非常好!!\n')
f.close()

# 只读方式打开文件，文件的指针将会放在文件的开头。
f = open('./data/test.txt', 'r')
s = f.read()
print(s)

f = open('./data/test.txt', 'r')
print('读取一行')
s = f.readline()
print(s)

f = open('./data/test.txt', 'r')
print('读取多行')
s = f.readlines(2)
print(s)

f = open('./data/test.txt', 'r')
print('迭代一个文件对象然后读取每行:')
for line in f:
    print(line,end='')
f.close()

# 打开文件，追加内容
f = open("./data/test.txt", "a+")
val = ['小明', '小张', '兰兰', 2]
f.write(str(val))
# 返回文件对象当前所处的位置, 它是从文件开头开始算起的字节数。
a = f.tell()
print('a = ', a)

s = f.read()
print('s = ', s)

# 如果要改变文件当前的位置, 可以使用 f.seek(offset, from_what) 函数。
f.seek(5) # 移动到文件的第六个字节
s = f.read(11)
print('s = ', s)
# 关闭文件并释放系统的资源
f.close()

# 当处理一个文件对象时, 使用 with 关键字是非常好的方式。在结束后, 它会帮你正确的关闭文件。
with open('./data/test.txt', 'r') as f:
    read_data = f.read()
    print(read_data)
f.close()

# python 的 pickle 模块实现了基本的数据序列和反序列化。
import pickle

# 使用 pickle 模块将数据对象保存到文件
data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}
print(data1)
selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)
print(selfref_list)
print('存入文件')
f = open('./data/test1.pkl', 'wb')

# Pickle dictionary using protocol 0.
pickle.dump(data1, f)

# Pickle the list using the highest protocol available.
pickle.dump(selfref_list, f, -1)
f.close()

#使用pickle模块从文件中重构python对象
f = open('./data/test1.pkl', 'rb')
print('读取文件')
data1 = pickle.load(f)
print(data1)

data2 = pickle.load(f)
print(data2)
f.close()

# python文件写入也可以进行网站爬虫
from urllib import request

response = request.urlopen('http://www.baidu.com/')     # 打开网站
f = open('./data/test2.txt', 'w')
n = f.write(str(response.read()))
print('n = ', n)
f.close()



