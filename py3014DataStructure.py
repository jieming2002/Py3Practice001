__author__ = 'skye2017-11-19'
# coding=utf-8

# 将列表当做堆栈使用
stack = [3,4,5] #左侧是栈底，右侧是栈顶，从栈顶出入栈
print('stack = ', stack)

stack.append(6) #在最右侧添加元素，从栈顶入栈
print('stack = ', stack)

stack.append(7)
print('stack = ', stack)

a = stack.pop() #从最右侧删除元素，从栈顶出栈
print('a = ', a)
print('stack = ', stack)

a = stack.pop()
print('a = ', a)
print('stack = ', stack)

# 将列表当作队列使用：效率不高
from collections import deque
queue = deque(['a', 'b', 'c'])
print('queue = ', queue)

queue.append('d')
queue.append('e')
print('queue = ', queue)

queue.popleft()
queue.popleft()
print('queue = ', queue)

# 列表推导式：提供了从序列创建列表的简单途径。
vec1 = [2, 4, 6]
print('vec1 = ', vec1)
# 将列表中每个数值乘三，获得一个新的列表
vec2 = [3*x for  x in  vec1]
print('vec2 = ', vec2)

# 现在我们玩一点小花样：
vec2 = [[x, x**2] for  x in vec1]
# vec2 =  [[2, 4], [4, 16], [6, 36]]
print('vec2 = ', vec2)

freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
# 对每个元素进行加工后，生成新列表
vec2 = [weapon.strip() for weapon in freshfruit]
print('vec2 = ', vec2)

vec1 = [2, 4, 6]
# 可以用 if 子句作为过滤器：
vec2 = [3*x for x in vec1 if x > 3]
print('vec2 = ', vec2)

# 以下是一些关于循环和其它技巧的演示：
vec1 = [2, 4, 6]
vec2 = [4, 3, -9]
vec3 = [x*y for x in vec1 for y in vec2]
print('vec3 = ', vec3)

vec3 = [vec1[i]*vec2[i] for i in range(len(vec1))]
print('vec3 = ', vec3)

# 列表推导式可以使用复杂表达式或嵌套函数：
vec3 = [str(round(355/113, i)) for i in range(1, 6)]
print('vec3 = ', vec3)

# 集合也支持推导式：
a = {x for x in 'abracadabra' if x not in 'abc'}
print('a = ', a)

# 构造函数 dict() 直接从键值对元组列表中构建字典。
d = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print('d = ', d)

# 字典推导可以用来创建任意键和值的表达式词典：
d = {x: x**2 for x in (2,4,6) if x < 5}
print('d = ', d)

# 如果关键字只是简单的字符串，使用关键字参数指定键值对有时候更方便：
d = dict(sape=4139, guido=4127, jack=4098)
print('d = ', d)

# 在字典中遍历时，关键字和对应的值可以使用 items() 方法同时解读出来：
knights = {'gallahad':1, 'robin':2}
for k,v in knights.items():
    print(k,v)

# 在序列中遍历时，索引位置和对应值可以使用 enumerate() 函数同时得到：
for i,v in enumerate(['a','b','c']):
    print(i,v)

# 同时遍历两个或更多的序列，可以使用 zip() 组合：
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q,a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

# 要反向遍历一个序列，首先指定这个序列，然后调用 reversed() 函数：
for i in reversed(range(1, 11, 2)):
    print(i)

# 要按顺序遍历一个序列，使用 sorted() 函数返回一个已排序的序列，并不修改原值：
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)



