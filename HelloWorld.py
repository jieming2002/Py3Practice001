__author__ = 'skye'
# coding=uft-8
# 因为代码中包含中文，所以需要加上上面这句，而且最好加在最上面，不然会报错。
# 值得一提的是默认情况下，代码中有中文需要注意，不光是在运行时，在运行后也是需要设置的，因为默认的输出中文会乱码。
# 大家可以在这里设置。File>>Settings>>Editor>>File Encodings>>Project Encodings 改成UTF-8

print("hello world 你好")

# 1.定义变量
x=1
y=2
z=x+y
print(z)

# 2.判断语句
score=90
# 每个条件后面需要加上冒号
if score>=90:
    # 判断语句后面的执行语句，默认不会有{}来确定开始和结束，非常简单，
    # 就是从条件语句后面的第一个缩进开始，最后一个缩进结束。
    print('你真棒')
    print('优秀')
# elif 相当于 else if
elif score>=80:
    # 判断条件后面的执行语句必须得有缩进
    print('良好')
elif score>=60:
    print('及格')

# 3.循环语句
for i in range(0,3): # range 表示范围，i 的范围在 0<=i<3
    print(i)
    # Python 不支持直接使用 + 这种语法
    # print("index"+i)
    # 字符串拼接，正确的语法是用 .format 支持多个拼接，但是需要与前面的 {} 的索引对应
    print("index {0} {1}".format(i,"cnblogs"))
print("end") # for 循环执行代码结束的标志就是结束缩进

# 4.定义函数 def
def HelloCNBlogs(): # 无论函数、循环或判断，都记得在语句后面加上冒号，冒号加上执行代码缩进表示开始
    # 不用 { } 来限定函数的开始和结束，通过缩进表示
    print('Hello cnblogs')

# 参数不用声明数据类型
def GetMax(x,y):
    if x>y:
        return x
    else:
        return y
# 无论函数、判断或循环，都是以没有缩进表示结束的

HelloCNBlogs()
print(GetMax(9,3))
print(GetMax('ab','vb'))

# 5.面向对象 class
class FirstTest: # 类也是冒号加缩进，表示开始
    # 这是类的构造函数，self 类似其他语言的 this
    def __init__(self,name):
        self._name=name # 一行就是一句，末尾不用分号，一句要分成多行才需要特殊符号处理 \
    def SayFirst(self):
        print('hello {0}'.format(self._name))
F=FirstTest("唐胜凯") # 实例化，因为构造函数里有个参数，所以传入一个参数。self 不算参数
F.SayFirst()

# 6.继承
class SecondTest(FirstTest): # 基类写在括号中
    def __init__(self,name):
        FirstTest.__init__(self,name) # 调用父类的构造函数
    def SaySecond(self):
        print('你好 {0}'.format(self._name))
S=SecondTest("唐胜凯") # 实例化
S.SayFirst() # 调用继承的父类方法
S.SaySecond() # 自己定义的方法
