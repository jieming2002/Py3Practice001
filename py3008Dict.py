__author__ = 'skye2017-11-18'
# coding=utf-8
# 字典的键必须是不可变的，如字符串，数字或元组。不能是列表、字典。
dict1 = {1:'小明', 3:'李兰', 21:'妲己'}
print('dict1 = {0}'.format(dict1))

dict1.clear() #清空字典，字典还在，内容没了
print('dict1 = {0}'.format(dict1))

# 不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住
dict1 = {1:'小明', 3:'李兰', 21:'妲己', 1:'星光'}
print('dict1 = {0}'.format(dict1))

a = len(dict1)
print('a = {0}'.format(a))

a = type(dict1)
print('a = {0}'.format(a))

#返回一个字典的浅复制 :
# 浅复制，我理解为只复制字典对象，而不复制字典里的内容，也就是说字典里的内容仍然是同一个内存地址
dict2 = dict1.copy()
print('dict2 = {0}'.format(dict2))

s = 'anaconda'
dict1 = dict.fromkeys(s) # 创建一个新字典，以序列中元素做字典的键，val为字典所有键对应的初始值
print('dict1 = {0}'.format(dict1))

a = dict1.get('b') #返回指定键的值，
print('a = {0}'.format(a))

list1 = dict1.items()
print('dict1.items = {0}'.format(list1))
list1 = list(list1)
print('list1 = {0}'.format(list1))
list1.sort()
print('list1 = {0}'.format(list1))
print('list1[:2] = {0}'.format(list1[:2]))
print('list1[-2:] = {0}'.format(list1[-2:]))

list1 = dict1.keys()
print('list1 = {0}'.format(list1))

dict2.update(dict1) #把字典 dict1 的键/值对更新到 dict2 里
print('dict2 = {0}'.format(dict2))

list1 = dict1.values()
print('list1 = {0}'.format(list1))

dict1.pop('a') # 删除字典给定键 key 所对应的值，
print('dict1 = {0}'.format(dict1))

dict1.popitem() # 随机返回并删除字典中的一对键和值(一般删除末尾对)。
print('dict1 = {0}'.format(dict1))


