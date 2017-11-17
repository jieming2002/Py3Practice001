__author__ = 'skye2017-11-16'
# coding=utf-8

# Python3 运算符
# 算术运算符：加减乘除，取模，不再重复

# 幂 - 返回x的y次幂
a = 2 ** 3
print('a = {0}'.format(a))

# 取整除 - 返回商的整数部分
a = 9 // 2
print('a = {0}'.format(a))
a = 9.0 // 2.0
print('a = {0}'.format(a))

# 比较运算符 == != > < >= <=
# 赋值运算符 就是算术运算符加上=
# 位运算符
a = 0b00111100
b = 0b00001101
print('a = {0}'.format(bin(a)))
print('b = {0}'.format(bin(b)))
print('a & b = {0}'.format(bin(a & b)))
print('a | b = {0}'.format(bin(a | b)))     # 按位或运算符
print('a ^ b = {0}'.format(bin(a ^ b)))     # 按位异或运算符：当两对应的二进位相异时，结果为1
print('~a = {0}'.format(bin(~a)))           # 按位取反
print('a << 2 = {0}'.format(bin(a << 2)))   # 左移位
print('a >> b = {0}'.format(bin(a >> 2)))   # 右移位

# 逻辑运算符 and or not
a = 10
b = 20
if (a and b): # 布尔"与"
    print('变量 a 和 b 都为 true')
else:
    print('变量 a 和 b 有一个不为 true')

if (a or b): # 布尔"或"
    print('变量 a 和 b 都为 true，或其中一个变量为 true')
else:
    print('变量 a 和 b 都不为 true')

# 修改变量 a 的值
a = 0

if (a and b):
    print('变量 a 和 b 都为 true')
else:
    print('变量 a 和 b 有一个不为 true')

if (a or b):
    print('变量 a 和 b 都为 true，或其中一个变量为 true')
else:
    print('变量 a 和 b 都不为 true')

if not (a and b): # 布尔"非"
    print('变量 a 和 b 都为 false，或其中一个变量为 false')
else:
    print('变量 a 和 b 都为 true')

# 成员运算符 in, not in 是否在指定的序列中
a = 1
b = 12
list1 = [1, 2, 3, 4]
print('a = {0}'.format(a))
print('b = {0}'.format(b))
print('list1 = {0}'.format(list1))

if (a in list1):
    print('变量 a 在给定的列表 list1 中')
else:
    print('变量 a 不在给定的列表 list1 中')

if (b not in list1):
     print('变量 b 不在给定的列表 list1 中')
else:
     print('变量 b 在给定的列表 list1 中')

# 身份运算符: 用于比较两个对象的存储单元 is , is not
# 注： id() 函数用于获取对象内存地址
print('id(a) = {0}'.format(id(a)))
a = 20
b = 20

if ( a is b ):
   print ("1 - a 和 b 有相同的标识")
else:
   print ("1 - a 和 b 没有相同的标识")

if ( id(a) == id(b) ):
   print ("2 - a 和 b 有相同的标识")
else:
   print ("2 - a 和 b 没有相同的标识")

'''
python 中，变量是以内容为基准而不是像 c 中以变量名为基准，
所以只要你的数字内容一样，不管你起什么名字，这个变量的 ID 是相同的，
同时也就说明了 python 中一个变量可以以多个名称访问。
这样的设计逻辑决定了 python 中数字类型的值是不可变的。
所以没有自增运算符 a++ 或 a--
因此，正确的自增操作应该 a = a + 1 或者 a += 1，
当此 a 自增后，通过 id() 观察可知，id 值变化了，即 a 已经是新值的名称。

楼上的同学所说的在脚本式编程环境中没有问题。
但是在交互式环境中，编译器会有一个小整数池的概念，会把（-5，256）间的数预先创建好，
而当a和b超过这个范围的时候，两个变量就会指向不同的对象了，因此地址也会不一样，
'''

# 修改变量 b 的值
b = 30
if ( a is b ):
   print ("3 - a 和 b 有相同的标识")
else:
   print ("3 - a 和 b 没有相同的标识")

if ( a is not b ):
   print ("4 - a 和 b 没有相同的标识")
else:
   print ("4 - a 和 b 有相同的标识")

'''is 与 == 区别：
is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。
'''
#  python 没有自增运算符，自增操作是如何实现的
print('a = {0}'.format(a))
a += 1
print('a = {0}'.format(a))
