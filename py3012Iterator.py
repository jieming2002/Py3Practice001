__author__ = 'skye2017-11-19'
# coding=utf-8
import sys

# 迭代器是一个可以记住遍历的位置的对象。
list1 = [1, 2, 3, 4]
it = iter(list1)  # 创建迭代器对象
print(next(it)) # 输出迭代器的下一个元素

for x in it:
    print (x, end=" ")

'''
list1 = ['a', 'b', 'c', 'd']
it = iter(list1)
while True:
    try: # 捕获异常
        print(next(it))
    except StopIteration: # 处理异常
        print('迭代器到头了')
        sys.exit() # 这个会导致脚本停止执行
'''

# 使用了 yield 的函数被称为生成器（generator）。生成迭代器。
# 跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。
# 在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回yield的值。
# 并在下一次执行 next()方法时从当前位置继续运行。

def fibonacci(n):  # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        print('counter = ', counter)
        if counter > n:
            return
        yield a
        a, b = b, a+b
        counter += 1
f = fibonacci(10) # f 是一个迭代器，由生成器返回生成
print('f = ', f)

'''
while True:
    try:
        print(next(f), end=' ')
    except StopIteration:
        print('迭代器到头了')
        sys.exit()
'''

def fibonacci2(n):  # 不使用 yield - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if counter > n:
            return
       # yield a
        a, b = b, a+b
        print('fibonacci2 %d %d'% (a, b))
        counter += 1
f = fibonacci2(10) # 函数只是简单执行，没有返回迭代器
print('f = ', f)

'''什么情况下需要使用 yield？
一个函数 f 返回一个 list，这个 list 是动态计算出来的，并且这个 list 会很大，会非常的占用内存。
我们希望每次调用这个函数的时候一个一个的得到每个 list 元素，而不是直接得到一个完整的 list 来节省内存。
这个时候 yield 就很有用。
实际上是先生成了一个迭代器，每次运行时，会暂停并保存当前所有的运行信息。
然后使用这个迭代器，每次只返回一个计算结果，而不是一个完整的 list
'''




