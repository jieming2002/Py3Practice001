__author__ = 'skye2017-11-19'
# coding=utf-8

# 计算面积函数
def area(width, height):
    return width * height

w = 4
h = 5
print('area =', area(w, h))

# python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 是可以修改的对象。
# 不可变类型
a = 5
a = 10 # 这里实际是在内存中新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变内存中 a 的值。

# 可变类型
la = [1, 2, 3, 4]
la[2] = 5 # 将列表 la 的第三个元素值更改，列表本身在内存中没有动，只是其内部的元素被修改了。

'''python 函数的参数传递
不可变类型：值传递，在 fun（a）内部修改 a 的值，只是修改另一个复制的对象，不会影响 a 本身。
可变类型：引用传递，fun（la） 是将 la 真正的传过去，修改后 fun 外部的 la 也会受影响。
python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。
'''

'''参数类型：
必需参数——以正确的顺序传入函数
关键字参数——允许函数调用时参数的顺序与声明时不一致
默认参数——函数定义时，设置了默认值
不定长参数——声明时不会命名。加了星号（*）的变量名会存放所有未命名的变量参数。
'''
def printMe(str1, str2, str3):
    print('str1 = ', str1)
    print('str2 = ', str2)
    print('str2 = ', str3)
    return

printMe(str2='我来了', str3='你是谁', str1='小明')

def printInfo(name, age=3):
    print('姓名：', name)
    print('年龄：', age)
    return

printInfo('小明')

def printInfo2(arg1, *varTuple):
    print('输出：', arg1)
    for var in varTuple:
        print(var)
    return

printInfo2(10)
printInfo2(10, 90, 4, 5, 6)

'''匿名函数: 使用 lambda 来创建
所谓匿名，意即不再使用 def 语句这样标准的形式定义一个函数。
lambda 只是一个表达式，函数体比 def 简单很多。
lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。
lambda [arg1 [,arg2,.....argn]]:expression
'''
# 函数声明
sum2 = lambda arg1, arg2: arg1 + arg2;

# 调用 sum2 函数
print('相加后的值为 :', sum2(10, 20))
print('相加后的值为 :', sum2(22, 11))

'''Python的变量作用域一共有4种：
L （Local） 局部作用域
E （Enclosing） 闭包函数外的函数中
G （Global） 全局作用域
B （Built-in） 内建作用域

以 L –> E –> G –>B 的规则查找，即：
在局部找不到，便会去局部外的局部找（例如闭包），再找不到就会去全局找，再者去内建中找。
'''
x = int(2.9) # int 是内建作用域
print('x = ', x)

g_count = 3 # g_count 是全局作用域
print('g_count = ', g_count)

def outer():
    o_count = 3.3  # o_count 闭包函数外的函数中
    # print('i_count = ', i_count) # 访问局部变量报错
    def inner():
        print('o_count = ', o_count) # 访问的是外部的闭包变量
        i_count = 55 # 局部作用域
        print('i_count = ', i_count) # 只能在这里访问这个局部变量
    inner() # 调用子函数

outer() # 调用自定义函数

'''Python 中只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，
其它的代码块（如 if/elif/else/、try/except、for/while等）是不会引入新的作用域的，
也就是说这这些语句内定义的变量，外部也可以访问，
'''
if True:
    msg = '我来自中国'
print(msg) #如果将 msg 定义在函数中，则它就是局部变量，外部不能访问

# 当内部作用域想修改外部作用域的变量时，就要用到 global 和 nonlocal 关键字了。
# 修改全局变量 num
num = 1
def fun1():
    global num # 需要使用 global 关键字声明
    print('num = ', num)
    num = 12
    print('num = ', num)
fun1()

# 要修改嵌套作用域（enclosing 作用域，外层非全局作用域）中的变量则需要 nonlocal 关键字
def outer2():
    print(msg)
    num = 10
    print('outer2 num = ', num)
    def inner2():
        nonlocal num # nonlocal关键字声明。否则外部的 num 值不变
        num = 100
        print('inner2 num = ', num)
    inner2()
    print('outer2 num = ', num)
outer2()

# lambda 匿名函数也可以使用"关键字参数"进行参数传递
g = lambda x,y:x**3 + y**2
a = g(2,3)
print('a = ', a)
a = g(x=3,y=2)
print('a = ', a)

