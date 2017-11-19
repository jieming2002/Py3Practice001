__author__ = 'skye2017-11-19'
# coding=utf-8

n = 100
sum2 = 0
counter = 1
while counter <= n:
    sum2 = sum2 + counter
    counter += 1
print('1 到 %d 之和为: %d' % (n, sum2))

n = 100
sum2 = 0
while n > 0:
    sum2 = sum2 + n
    n -= 1
print('1 到 100 之和为: %d' % (sum2))

# 无限循环: 为什么需要无限循环？ 无限循环在服务器上客户端的实时请求非常有用。
while True:
    num = float(input('输入一个数字:'))
    print('你输入的数字是: ', num)
    if num == 1:
        break
# 可以使用 CTRL+C 来退出当前的无限循环。
print ("Good bye!")

# while 循环使用 else 语句
count = 0
while count < 5:
    print(count, ' 小于 5')
    count += 1
else:  # 在条件语句为 false 时执行 else 的语句块
    print(count, ' 大于或等于 5')

lan = ['c', 'c++', 'c#', 'python', 'R']
for a in  lan:
    print(a)
else:
    print('结束啦')

# range()函数 遍历数字序列
for i in range(5): # 0~4
    print(i)

# 使用range指定区间的值：
for i in range(5, 9): # 5~8
    print(i)

# 指定不同的增量(甚至可以是负数，有时这也叫做'步长'):
for i in range(0, 10, 3):
    print(i)
for i in range(-10, -110, -30):
    print(i)

# 使用range()函数来创建一个列表
l = list(range(4))
print(l)

# 循环语句可以有 else 子句，它在穷尽列表(以for循环)或条件变为 false (以while循环)导致循环终止时被执行,
# 但循环被break终止时不执行。
# pass 语句,是空语句，是为了保持程序结构的完整性。不做任何事情，一般用做占位语句，
class MyEmptyClass:
    pass

if a == 1:
    pass # 这个 pass 语句的确很有用，有时候我们不想判断 a != 1 那么这里就留空白，有个 pass 在这里占位
else:
    print('a 不等于 1')

# 使用内置 enumerate 函数进行遍历:
lan = ['c', 'c++', 'c#', 'python', 'R']
for index, item in enumerate(lan):
    print(index, item)



