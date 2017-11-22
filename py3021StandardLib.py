__author__ = 'skye 2017-11-22'
# coding=utf-8

import os
# os 模块提供了不少与操作系统相关联的函数。
def testOS():
    s = os.getcwd()  # 返回当前的工作目录
    print(s)
    # 在使用 os 这样的大型模块时内置的 dir() 和 help() 函数非常有用:
    print(dir(os)) # 返回所有模块和函数的名称列表
    # print(help(os)) # 返回帮助页面，非常详细

# 针对日常的文件和目录管理任务，:mod:shutil 模块提供了一个易于使用的高级接口:
import shutil
def testShutil():
    shutil.copy('./data/test.txt', './data/test copy.txt')

# glob 模块提供了一个函数用于从目录通配符搜索中生成文件列表:
import glob
def globTest():
    g = glob.glob('./data/*.txt')
    print(g)

# 命令行参数 以链表形式存储于 sys 模块的 argv 变量。
import sys
def testSys():
    print(sys.argv)
    print(sys.stdin)
    print(sys.stdout)
    print(sys.stderr)

# re 模块为高级字符串处理提供了正则表达式工具。对于复杂的匹配和处理，正则表达式提供了简洁、优化的解决方案:
import re
def testRE():
    # 在字符串中查找以 f 开头的单词：分词技术
    s = re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest?')
    print(s)

    s = re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
    print(s)

    # 如果只需要简单的功能，应该首先考虑字符串方法，因为它们非常简单，易于阅读和调试:
    s = 'tea for too'.replace('too', 'two')
    print(s)

# math模块为浮点运算提供了对底层C函数库的访问:
import math
def testMath():
    a = math.cos(math.pi / 4)
    print(a)
    a = math.log(1024, 2)
    print(a)

    # random 提供了生成随机数的工具。
    import random
    a = random.choice(['apple', 'pear', 'banana'])
    print(a)

    a = random.sample(range(100), 10)
    print(a)

    a = random.random()
    print(a)

    a = random.randrange(6)
    print(a)

# 有几个模块用于访问互联网以及处理网络通信协议
from urllib.request import urlopen
import smtplib

def testNet():
    for line in urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl'):
        line = line.decode('utf-8')   # Decoding the binary data to text.
        if 'EST' in line or 'EDT' in line:
            print(line)

    # 需要本地有一个在运行的邮件服务器。
    server = smtplib.SMTP('localhost')
    server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
                    '''To: jcaesar@example.org
                    From: soothsayer@example.org
                    Beware the Ides of March.
                    ''')
    server.quit()

# datetime模块为日期和时间处理同时提供了简单和复杂的方法。
from datetime import date
def testDateTime():
    now = date.today()
    print(now)
    s = now.strftime("%M-%D-%Y. %m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
    print(s)

    birthday = date(1988, 8, 1)
    print(birthday)
    age = now - birthday
    print(age)
    print(age.days)

# 以下模块直接支持通用的数据打包和压缩格式：zlib，gzip，bz2，zipfile，以及 tarfile。
import zlib
def testZip():
    s = b'witch which has which witches wrist watch'
    print('字符串长度：', len(s))
    t = zlib.compress(s)
    print('压缩后：', len(t))
    print(t)
    s = zlib.decompress(t)
    print(s)
    t = zlib.crc32(s)
    print(t)

# 性能度量 Python 提供了一个工具度量, 解决同一问题的不同方法之间的性能差异
from timeit import Timer
def testTimer():
    # 使用元组封装和拆封来交换元素看起来要比使用传统的方法要诱人的多
    t = Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
    print(t)
    t = Timer('a,b = b,a', 'a=1; b=2').timeit()
    print(t)
    # timeit 证明了现代的方法更快一些。
# 相对于 timeit 的细粒度，:mod:profile 和 pstats 模块提供了针对更大代码块的时间度量工具。

# doctest 模块提供了一个工具，扫描模块并根据程序中内嵌的文档字符串执行测试。
import doctest
def average(values):
    ''' 计算数值序列的算术平均值
    :param values: 数值序列
    :return: 算术平均值

    >>> print(average([20, 30, 70]))
    40.0
    '''
    return sum(values) / len(values)

def testDoc():
    # a = average([20, 30, 70])
    # print(a)
    s = doctest.testmod() # 自动验证嵌入测试
    print(s)

# unittest 模块不像 doctest 模块那么容易使用，不过它可以在一个独立的文件里提供一个更全面的测试集:
import unittest
class TestStatisticalFunctions(unittest.TestCase):
    def testAverage(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        self.assertRaises(ZeroDivisionError, average, [])
        self.assertRaises(TypeError, average, 20, 30, 70)

def testUnit():
    s = unittest.main() # 调用所有的测试

# 从这里开始执行代码
if __name__ == '__main__':
    # testMath()
    # testNet()
    # testDateTime()
    # testZip()
    # testTimer()
    # testDoc()
    testUnit()
