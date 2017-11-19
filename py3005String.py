__author__ = 'skye2017-11-18'
# coding=utf-8
# Python 不支持单字符类型，单字符也是作为一个字符串使用。

# Python 支持格式化字符串的输出 。
print('我叫 %s 今年 %d 岁' % ('小明', 10))
# 格式化符号必须与数据类型匹配
# 三引号让程序员从引号和特殊字符串的泥潭里面解脱出来
s = 'beijing'
print('s = {0}'.format(s))

s = s.capitalize()
print('s = {0}'.format(s))

s = s.center(22)
print('s = {0}'.format(s))

s = s.count('i')
print('s = {0}'.format(s))

s = 'beijing'
s = s.encode()
print('s = {0}'.format(s))

s = s.decode()
print('s = {0}'.format(s))

s = s.endswith('a')
print('s = {0}'.format(s))

s = '   bei jing'
print('s = {0}'.format(s))
s = s.expandtabs(16)
print('s = {0}'.format(s))

s = s.find('i')
print('s = {0}'.format(s))

s = 'BEIJING'
print('s = {0}'.format(s))
s = s.lower()
print('s = {0}'.format(s))

# 使用格式化符号进行进制转换
a = 111
print('十六进制：%x' % a) # 使用%x将十进制num格式化为十六进制
print('十六进制：%#x' % a) # 多加入了一个#号，目的是在转换结果头部显示当前进制类型

print('八进制：%#o' % a) # 使用%o将十进制num格式化为八进制
print('二进制：', bin(a)) # 使用bin将十进制num格式化为二进制

# [::2] 表示的是从头到尾，步长为2。
# 第一个冒号两侧的数字是指截取字符串的范围,第二个冒号后面是指截取的步长。
s = 'abcdefghijk'
s = s[::2]
print('s = {0}'.format(s))

# 字符串的分割还有partition()这种方式。
s1 = "I'm a good sutdent."
print('s1 = {0}'.format(s1))
s2 = s1.partition('good') # 以'good'为分割符，返回头、分割符、尾三部分。
print('s2 = {0}'.format(s2))
s3 = s1.partition('abc') # 没有找到分割符'abc'，返回头、尾两个空元素的元组
print('s3 = {0}'.format(s3))

