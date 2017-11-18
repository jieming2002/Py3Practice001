__author__ = 'skye2017-11-18'
# coding=utf-8

list1 = ['go', 'to', 1, 2]
print('list1 = {0}'.format(list1))
del list1[2] # 用 del 语句来删除列表的的元素
print('list1 = {0}'.format(list1))

a = len(list1) # 计算列表的长度
print('a = {0}'.format(a))
a = list1.__len__()
print('a = {0}'.format(a))

list1 = list1 + list1 # + 号用于组合列表
print('list1 = {0}'.format(list1))

list1 = ['go']
print('list1 = {0}'.format(list1))
list1 = list1 * 3 # * 号用于重复列表
print('list1 = {0}'.format(list1))

list1.append(2) # 在列表末尾添加新的对象
print('list1 = {0}'.format(list1))

a = list1.count('go') # 统计某个元素在列表中出现的次数
print('a = {0}'.format(a))

list1.extend((1,2,3)) # 在列表末尾一次性追加另一个序列中的多个值
print('list1 = {0}'.format(list1))

a = list1.index(2)
print('a = {0}'.format(a))

list1.insert(2, 'new') # 将对象插入列表
print('list1 = {0}'.format(list1))

a = list1.pop(2) # 移除列表中的一个元素
print('a = {0}'.format(a))
print('list1 = {0}'.format(list1))

list1.remove('go') # 移除列表中某个值的第一个匹配项
print('list1 = {0}'.format(list1))

list1.reverse() # 反向列表中元素
print('list1 = {0}'.format(list1))

list1 = [1,4,2,7,3,6,5]
print('list1 = {0}'.format(list1))
list1.sort() # 对原列表进行排序: 元素类型必须一致
print('list1 = {0}'.format(list1))

list1 = ['a', 'd', 's', 'b', 'm']
print('list1 = {0}'.format(list1))
list1.sort() # 对原列表进行排序: 元素类型必须一致
print('list1 = {0}'.format(list1))

list2 = list1.copy() # 复制列表：新的的内存地址
print('list2 = {0}'.format(list2))
print('id(list1) = {0}'.format(id(list1)))
print('id(list2) = {0}'.format(id(list2)))
# 也可以使用截取语法
list2 = list1[:] # 截取列表：新的的内存地址
print('list2 = {0}'.format(list2))
print('id(list1) = {0}'.format(id(list1)))
print('id(list2) = {0}'.format(id(list2)))

list1.clear()
print('list1 = {0}'.format(list1))

# python 创建二维列表，将需要的参数写入 cols 和 rows 即可
col = 3
row = 4
list2D = [[(i + j) for i in range(col)] for j in range(row)]
print('list2D = {0}'.format(list2D))

list1 = [i for i in range(15)]
print('list1 = {0}'.format(list1))
list2 = list1[::2] # [start:end:span] 当 span>0 时顺序遍历。start 不输入则默认为 0，end 不输入默认为长度。
print('list2 = {0}'.format(list2))
list2 = list1[::-2] # [start:end:span] 当 span<0 时，逆着遍历。 span 不能=0
print('list2 = {0}'.format(list2))

