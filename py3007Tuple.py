__author__ = 'skye2017-11-18'
# coding=utf-8

# Python 的元组与列表类似，不同之处在于元组的元素不能修改。
tup1 = ('小明', '小刚', '卫华')
print('tup1 = {0}'.format(tup1))

# 元组中只包含一个元素时，需要在元素后面添加逗号，否则括号会被当作运算符使用：
tup1 = (23) # 这样得到的是一个整数 int
print('tup1 = {0}'.format(tup1))
tup1 = (23,)  # 加上逗号，类型为元组
print('tup1 = {0}'.format(tup1))

# 元组与字符串类似，下标索引从0开始，可以进行截取，组合等。
# 元组中的元素值是不允许修改的，但我们可以对元组进行连接组合
tup2 = (88, 91, 66)
print('tup2 = {0}'.format(tup2))

tup3 = tup1 + tup2 # 组合两个元组，创建新的元组
print('tup3 = {0}'.format(tup3))

tup3 = tup2 * 3 # 把元组 tup2 赋值三份，放入新元组
print('tup3 = {0}'.format(tup3))

a = len(tup3) # 计算序列的长度
print('a = {0}'.format(a))

a = max(tup3) #返回元组中元素最大值。
print('a = {0}'.format(a))

list1 = ['小明', '李兰', '卫华']
print('list1 = {0}'.format(list1))
tup1 = tuple(list1) # 将列表转换为元组
print('tup1 = {0}'.format(tup1))

# 不可变的tuple有什么意义？因为tuple不可变，所以代码更安全。
# 如果可能，能用tuple代替list就尽量用tuple。




