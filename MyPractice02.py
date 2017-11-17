__author__ = 'Skye.Tang 2017-10-28'
# 1. Python的常量相对其他语言，可能略显麻烦。
# 不仅仅只是单靠const就可以完成常量定义的。在Python中定义常量需要用对象的方法来创建。
# 我们需要在Lib的目录下创建一个const.py的文件。
import const # 引入常量类
const.value=5 # 给常量类添加常量 value
print(const.value)
# const.value=7 # 再对 value 赋值，会报错
const.maxVal=15 # 给常量类添加常量 maxVal
print(const.maxVal)
# print(const.minVal) # 没有给常量类添加常量，直接读取，会报错

# 2.数的类型：复数
print(complex(1))
print(complex('3+89j'))
print(complex(4,5))

l=[1,2,4,7]
for i in l:
    print(complex(i,7))

# 3.字符串类型
# 单引号字符串：单引号和双引号可以交叉使用
s1='hello "baby" \n'
# 双引号字符串：可以包含单引号，而不需要转义
s2="hello,'baby' U can't do it \n"
# 三引号字符串：可由多行组成，输出时，会保持原格式。可以包含单引号，而不需要转义
s3="""hello everyone,
good morning. "baby" can't do it \n"""
s4='''hello Kitty,
good evening."baby"  U can't do it.
what can you see?\n'''
print(s1+s2+s3+s4)

# 4.转义符和换行符
s1='I\'m yong'
print(s1)
s2="Our young.\nDo you know?"
print(s2)

# 5.自然字符串和字符串重复
# 自然字符串字面意思理解就是将字符串保留本身的格式，而不受转义的影响。原样输出。
s1=r'Our \nyoung.'
print(s1)
# 不是自然字符串，转义符会影响。
s2='Our \nyoung.'
print(s2)
# 字符串重复,字面意思理解就是将字符串重复输出。居然可以这样 *3 输出 3 次
s3='Our young. 1\n'*3
print(s3)

# 6.子字符串
s='Morning young.\n'
# 索引为 0 的字符
s1=s[0]
print('s1='+s1)
# 索引为 8 的字符
s2=s[8]
print('s2='+s2)
# 从 0 开始截取到索引为 3-1 的字符
s3=s[:3]
print('s3='+s3)
# 从索引 3 开始截取到最后的字符串
s4=s[3:]
print('s4='+s4)
# 从索引 3 开始截取到索引为 6-1 的位置
s5=s[3:6]
print('s5='+s5)

# 7.数据类型
# 列表：python里没有数组的概念，列表和数组的概念很接近。列表是用来存储一连串元素的容器，用[]表示。
people=['李园艳','张三','李四','王五','赵六']
print(people[3])
print(people)
# 元组：同样，元组和数组的概念也很接近，用()表示。另外元组只能读取不能修改。
names=('李园艳','张三','李四','王五','赵六')
print(names[1])
print(names)
# 集合：
# 格式：set(元素)，python的集合是一个无序不重复元素集。
# 功能：建立关系； 消除重复元素
# 集合默认是去除重复的
set1=set('122222334567890')
print('set1='+str(set1))
# 增加元素
set1.add('a')
print('set1='+str(set1))
# 删除已有元素，如果没有会返回异常
set1.remove('2')
print('set1='+str(set1))
# 如果存在元素，就删除，没有不报异常
set1.discard('2')
print('set1='+str(set1))
set2=set('abc')
# 交集：两种写法
print('交集：'+str(set1 & set2))
print('交集：'+str(set1.intersection(set2)))
# 并集：两种写法
print('并集：'+str(set1 | set2))
print('并集：'+str(set1.union(set2)))
# 差集：两种写法
print('差集：'+str(set1 - set2))
print('差集：'+str(set1.difference(set2)))
set1.pop() # 随机删除一个元素
print('set1='+str(set1))
# 清空集合
set1.clear()
print('集合被清空 set1='+str(set1))

# 字典：Python中的字典也叫关联数组，用{}表示。
# 这里可以用单引号，也可以双引号
dic={'name':"skye", 'age':'33','sex':'man'}
print(dic['name'])
print(dic)
# 向字典中添加项目
dic['hobby']='cnblogs'
print(dic)

# 8.标识符：编程时使用的名字，比如变量、常量、函数、语句块的名字；我们统统称之为标识符。
# python中的关键字是指系统中自带的具备特定含义的标识符。
# 标识符命名规范：
# 必须只能是字母或下划线开头，不能是数字或者其他字符开头
# 除第一个开头字符外，其他部分可以是字母或者下划线或者数字
# 标识符大小写敏感，比如name和Name是不一样的标识符

# 9.对象：在Python中，一切都可以看做是对象。
# Pyhon的内置对象：1数字、2字符串、3列表、4元组、5字典、6集合等等