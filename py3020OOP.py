__author__ = 'skye 2017-11-22'
# coding=utf-8

class Complex: #定义一个类：复数
    def __init__(self, realPart, imagPart):
        '''
        类的构造函数，注意这个函数接受两个参数，而不是三个。
        类的方法与普通的函数只有一个特别的区别——
        它们【必须】有一个额外的第一个参数名称, 按照惯例它的名称是 self
        self 代表的是类的实例，代表当前对象的地址，而 self.__class__ 则指向类。
        self 不是 python 关键字，我们把他换成 runoob 也是可以正常执行的:

        类方法必须包含参数 self, 且为第一个参数，self 代表的是类的实例。
        :param realPart:
        :param imagPart:
        '''
        self.r = realPart
        self.i = imagPart
        print(self.__class__)

def testComplex():
    x = Complex(3.0, 4.5)
    print(x.r, x.i)

class people:
    #定义基本属性
    name = ''
    age = 0
    #定义私有属性,两个下划线开头
    __weight = 0
    #定义构造方法：类方法必须包含参数 self，且为第一个参数，self 代表的是类的实例。
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print('{0} 说：我 {1} 岁。'.format(self.name, self.age))

'''单继承示例，基类在圆括号中
需要注意基类的顺序，若是基类中有相同的方法名，而在子类使用时未指定，
python 从左至右搜索 即方法在子类中未找到时，从左到右查找基类中是否包含方法。
'''
class student(people):
    grade = 0
    def __init__(self, n, a, w, g):
        # 调用父类的构造函数
        people.__init__(self, n, a, w)
        self.grade = g
    #覆写父类的方法
    def speak(self):
        print('{0} 说：我 {1} 岁了，我在读 {2} 年级。'.format(self.name, self.age, self.grade))

def testStudent():
    s = student('小唐', 12, 23, 5)
    s.speak()

#另一个类，多重继承之前的准备
class speaker:
    topic = ''
    name = ''
    def __init__(self, n, t):
        self.name = n
        self.topic = t
    def speak(self):
        print('我叫 {0} 我是一个演说家，演讲的主题是：{1}'.format(self.name, self.topic))

#多重继承：把基类的顺序调整一下看看
class superStudent(student, speaker):
    a = ''
    def __init__(self, n, a, w, g, t):
        student.__init__(self, n, a, w, g)
        speaker.__init__(self, n, t)
    # 私有方法，也是两个下划线开头
    def __write(self):
        print('写作文')
    # 我们可以对类的专有方法进行重载
    def __str__(self): # 返回类的字符串信息
        return '超级学生：{0}，年龄：{1}，年级：{2}，演讲主题：{3}'.format(self.name, self.age, self.grade, self.topic)
    def __add__(self, other): #计算两个类实例的和，加法
        return superStudent(self.name + other.name,
                            self.age + other.age,
                            99,
                            self.grade + other.grade,
                            self.topic + other.topic)

def testSuperStudnet():
    s = superStudent('小明', 22, 55, 9, '人生')
    s.speak()  #方法名同，默认调用的是在括号中排前地父类的方法
    s2 = superStudent('小唐', 23, 66, 11, '人工智能')
    print(s + s2)

# 从这里开始执行代码，上面负责定义
if __name__ == '__main__':
    # testComplex()
    # testStudent()
    testSuperStudnet()


