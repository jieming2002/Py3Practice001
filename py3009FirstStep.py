__author__ = 'skye2017-11-18'
# coding=utf-8

# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
a, b = 0, 1
while b < 10:
    print(b)
    a, b = b, a+b

# end 关键字: 用于将结果输出到同一行，或者在输出的末尾添加不同的字符，
a, b = 0, 1
while b < 111:
    print(b, end=', ')
    a, b = b, a+b

# print() sep 参数使用
a, b, c = 23, 33, 34
print(a, b, c, sep='@')

