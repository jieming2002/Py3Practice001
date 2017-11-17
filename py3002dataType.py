__author__ = 'skye2017-11-15'
# coding: utf-8 用于 Unicode 编码，显示中文

'''
Python 中的变量不需要声明。
每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。
在 Python 中，变量就是变量，它没有类型，我们所说的"类型"是变量所指的内存中对象的类型。
变量名就是一个符号，没有实际意义，变量值才是实际的。
正如一个人，你的名字无所谓，你的思想和身体才是实际的，决定你的行为和结果。
'''
s = '你好' # 字符串 str 类型
print(s)
print('type(s) = {0}'.format(type(s)))

s = 23 # 变成了 int 类型
print(s)
print('type(s) = {0}'.format(type(s)))

s = 2.3 # 变成了 float 类型
print(s)
print('type(s) = {0}'.format(type(s)))

# Python允许你同时为多个变量赋值。
# 可以是多对一
a = b = c = 1
# 也可以为多个对象指定多个变量。多对多。
a, b, c = 1, 2, '新鲜语法'
print('a = {0}, b = {1}, c = {2}'.format(a, b, c))
# 还可以 一对多
a = 1, 2, '新鲜语法'
print('a = {0}'.format(a))

'''Number（数字）
Python3 支持 int、float、bool、complex（复数）。
把布尔值归类到了数字
'''
a, b, c, d = 23, 2.3, False, 2+3j
print(type(a), type(b), type(c), type(d))

# 可以用 isinstance 来判断：变量是否属于某个数据类型
flag = isinstance(a, int)
print('a is int = {0}'.format(flag))

''' isinstance 和 type 的区别在于：
type 比 isinstance 更精确，对于子类和父类的实例，
isinstance 都是 True
type 值不同

type 主要用于判断未知数据类型，
isinstance 主要用于判断 A 类是否继承于 B 类：

注意：在 Python2 中是没有布尔型的，它用数字 0 表示 False，用 1 表示 True。
到 Python3 中，把 True 和 False 定义成关键字了，但它们的值还是 1 和 0，可以和数字相加。
'''

# 可以使用del语句删除一些对象引用
del a
# print('a = {0}'.format(a)) # 上面删除了 a 对象，这里报错 NameError: name 'a' is not defined
del b, c, d

# 新鲜表达式，乘方运算：2 的 5 次方
a = 2 ** 5
print('a = {0}'.format(a))
# 在混合计算时，Python会把整型转换成为浮点数。
# 复数的实部 a 和虚部 b 都是浮点型

# 字符串的截取，索引值以 0 为开始值，-1 为从末尾的开始位置。
a = '字符串的截取：变量[头下标:尾下标]'
print(a[0:-1]) # 输出第一个到倒数第二个的所有字符
print(a[0]) # 输出字符串第一个字符
print(a[2:5]) # 输出从第三个开始到第五个的字符
print(a[2:])  # 输出从第三个开始的后的所有字符
# 星号 (*) 表示复制当前字符串，紧跟的数字为复制的次数
print(a * 2)      # 输出字符串两次：这个很奇妙
print(a + ' 新来的') # 连接字符串
# 注意，Python 没有单独的字符类型，一个字符就是长度为1的字符串。
# 与 C 字符串不同的是，Python 字符串不能被改变。向一个索引位置赋值，比如 a[0] = 'm'会导致错误。

'''List（列表） 相当于 Array(数组)
列表中元素的类型可以不相同，
和字符串一样，列表同样可以被索引和截取，
'''
l = ['ab', 7, 2.3, '流量', 2.1]
tinyList = [9, 'hello']
print(l)                    # 输出完整列表
print(l[0])                 # 输出列表第一个元素
print(l[1:3])               # 从第二个开始输出到第三个元素
print(l[2:])                # 输出从第三个元素开始的所有元素
print(tinyList * 2)         # 输出两次列表: 星号（*）是重复操作， 这个和数组不同
print(l + tinyList)         # 连接列表: 加号（+）是列表连接运算符，这个和数组不同

# 与Python字符串不一样的是，列表中的元素是可以改变的：
tinyList[0] = 'hi'
print(tinyList)
tinyList.append(23)
print(tinyList)

'''Tuple（元组） 与List（列表） 有什么不同？
不同之处在于元组的元素不能修改。元组写在小括号(())里，
元组中的元素类型也可以不相同
'''
t = ('AB', 6, 2.1, '你好', 99.9)
tinyTuple = (3, '来了')

print(t)                # 输出完整元组
print(t[0])             # 输出元组的第一个元素
print(t[1:3])           # 输出从第二个元素开始到第三个元素
print(t[2:])            # 输出从第三个元素开始的所有元素
print(tinyTuple * 2)    # 输出两次元组
print(t + tinyTuple)    # 连接元组

# tinyTuple[0] = '密码' 不能修改，报错 TypeError: 'tuple' object does not support item assignment
print(tinyTuple)
# 虽然tuple的元素不可改变，但它可以包含可变的对象，比如list列表。
# 构造包含 0 个或 1 个元素的元组比较特殊，所以有一些额外的语法规则：
t = ()      # 空元组
t = (21,)   # 一个元素，需要在元素后添加逗号
# string、list 和 tuple 都属于 sequence （序列）。

'''Sets（集合）中的元素是无序的，不重复的。
注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
'''
student = {'tim', 'cat', 'dog', 'jack', 'mary', 'jack'}
tinySet = set('a')

print(student)      # 输出集合，重复的元素被自动去掉
print(tinySet)

# 成员测试
if ('lily' in student):
    print('lily 在集合中')
else:
    print('lily 不在集合中')

# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')

print('a = {0}'.format(a))
print('b = {0}'.format(b))
print('a - b = {0}'.format(a - b))      # a和b的差集
print('a | b = {0}'.format(a | b))      # a和b的并集
print('a & b = {0}'.format(a & b))      # a和b的交集
print('a ^ b = {0}'.format(a ^ b))      # a和b中不同时存在的元素

''' Dictionary（字典）
和 actionscript3 中的字典一样。 object 差不多
键(key)必须使用不可变类型。
'''
d = {}
d['one'] = '第一个工具'
d[2] = '第二个基础'
print(d)
print(d['one'])
print(d[2])

tinyDic = {'name':'jack', 'code':110, 'site':'www.runoob.com'}
print(tinyDic.keys())       # 输出所有键
print(tinyDic.values())     # 输出所有值

# 构造函数 dict() 可以直接从键值对序列中构建字典
d = dict([('tom', 1), ('jack', 2), ('rose', 3)])
print(d)

# 这是什么语法？key 是 x ，value 是 x 的平方，x 的取值范围是元组 (2, 4, 6)
d = {x:x**2 for x in (2, 4, 6)}
print(d)

d = dict(tim=1, lily=2, rode=3)
print(d)

# 数据类型转换
a = '02'
print(a)
b = int(a) # 将x转换为一个整数
print(b)

a = '0.2'
print(a)
b = float(a) # 将x转换到一个浮点数
print(b)

a = 2
print('a = {0}'.format(a))
b = complex(a) # 创建一个复数
print('b = {0}'.format(b))

a = (1, 2, 3)
print('a = {0}'.format(a))
b = str(a) # 将对象 x 转换为字符串
print('b = {0}'.format(b))

a = 'ab'
print('a = {0}'.format(a))
b = repr(a) # 将对象 x 转换为表达式字符串
print('b = {0}'.format(b))

a = '2 + 3'
print('a = {0}'.format(a))
b = eval(a) # 用来计算在字符串中的有效Python表达式,并返回一个对象
print('b = {0}'.format(b))

a = [1, 2, 3]
print('a = {0}'.format(a))
b = tuple(a) # 将序列 s 转换为一个元组
print('b = {0}'.format(b))

a = '345'
print('a = {0}'.format(a))
b = list(a) # 将序列 s 转换为一个列表
print('b = {0}'.format(b))

a = '345563'
print('a = {0}'.format(a))
b = set(a) # 转换为可变集合
print('b = {0}'.format(b))

a = [('a',1),('b',2),('c',3)]
print('a = {0}'.format(a))
b = dict(a) # 创建一个字典。d 必须是一个序列 (key,value)元组。
print('b = {0}'.format(b))

a = '345563'
print('a = {0}'.format(a))
b = frozenset(a) # 转换为不可变集合
print('b = {0}'.format(b))

a = 3
print('a = {0}'.format(a))
b = chr(a) # 将一个整数转换为一个字符
print('b = {0}'.format(b))

a = '3'
print('a = {0}'.format(a))
b = ord(a) # 将一个字符转换为它的整数值
print('b = {0}'.format(b))

a = 151
print('a = {0}'.format(a))
b = hex(a) # 将一个整数转换为一个十六进制字符串
print('b = {0}'.format(b))

a = 151
print('a = {0}'.format(a))
b = oct(a) # 将一个整数转换为一个八进制字符串
print('b = {0}'.format(b))

'''一般来说，函数的返回值一般为一个。
而函数返回多个值的时候，是以元组的方式返回的。
'''
def returnTuple(a, b):
    return (a,b)
a = returnTuple(2,3)
print(a)
print(type(a))

# 函数还可以接收可变长参数，比如以 "*" 开头的的参数名，会将所有的参数收集到一个元组上。
def changableArgument(*args):
    print(args)
    return args
print(type(changableArgument(1,2,3,4)))

''' 在list的使用中，开始时很容易忽视的一点是：
list[1:3] 其实输出的只有两个变量，即list中第二个元素到第三个元素，并不是第1 第2 第3三个元素
'''
'''
'''



