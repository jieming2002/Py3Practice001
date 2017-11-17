__author__ = 'Skye.Tang'
import math
import timeit

print('中文 Chinese')
# Python 3，有了 Unicode (utf-8) 字符串，以及一个字节类：byte 和 bytearrays。
# 由于 Python3.X 源码文件默认使用utf-8编码，这就使得以下代码是合法的：
中国='变量名是中文'
print(中国)
# str 是系统函数，不要用 str 作为变量名
a = "我爱北京天安门"
print(a)
b = '我爱北京天安门'
print(b)

# 除法：：Python中的除法有两个运算符，/和//
# python 3 中 / 除法不再把小数部分完全忽略掉，对于整数之间的相除，结果也会是浮点数。
a=22/3
print('22/3 = '+str(a))
b=2/2
print('2/2 = '+str(b))
# 对于 // 除法，叫做 floor 除法，会对除法的结果自动进行一个 floor 操作，在python 2.x和 python 3.x中是一致的。
a=22//3
print('22//3 = '+str(a))
b=-1//2
print('-1//2 = '+str(b))
# 注意的是：：并不是舍弃小数部分，而是执行 floor 操作，如果要截取小数部分，那么需要使用 math 模块的 trunc 函数
a=math.trunc(22/3)
print('math.trunc(22/3) = '+str(a))
b=math.trunc(-1/2)
print('math.trunc(-1/2) = '+str(b))

# xrange
print('Python',copyright())
print('\ntiming range()')

# 八进制字面量表示
""" 多行注释
八进制数必须写成 0o777，原来的形式 0777 不能用了；二进制必须写成 0b111
新增了一个bin()函数用于将一个整数转换成二进制字串。
"""
a=0o1000
print('八进制数 1000 ='+str(a))

""" 不等运算符
Python 2.x中不等于有两种写法 != 和 <>
Python 3.x中去掉了<>, 只有 != 一种写法
"""

"""去掉了repr表达式``
Python 2.x 中反引号``相当于repr函数的作用
Python 3.x 中去掉了``这种写法，只允许使用repr函数，这样做的目的是为了使代码看上去更清晰
用repr的机会很少，一般只在debug的时候才用，多数时候还是用str函数来用字符串描述对象
"""

""" 数据类型
Py3.X去除了long类型，现在只有一种整型——int，但它的行为就像2.X版本的long
新增了bytes类型，对应于2.X版本的八位串，定义一个bytes字面量的方法如下：
"""
b=b'china'
print('b = '+str(b))
# 获取变量的类型
c=type(b)
print('type(b) = '+ str(c))
# str对象和bytes对象可以使用.encode() (str -> bytes) or .decode() (bytes -> str)方法相互转化。
s=b.decode()
print('s = '+s)
b=s.encode()
print('b = '+str(b))

"""打开文件
原：
file( ..... )
或
open(.....)
改为只能用
open(.....)
"""

""" 从键盘录入一个字符串
在python2.x中raw_input()和input( )，两个函数都存在，其中区别为：
 raw_input()---将所有输入作为字符串看待，返回字符串类型
 input()-----只能接收"数字"的输入，在对待纯数字输入时具有自己的特性，它返回所输入的数字的类型（int, float）
在python3.x中raw_input()和input( )进行了整合，去除了raw_input()，仅保留了input()函数，
其接收任意任性输入，将所有输入默认为字符串处理，并返回字符串类型。
"""
input("请输入你的愿望：")
