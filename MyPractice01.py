import array

__author__ = 'Administrator'
# 7.引入其他文件的类
# 第一种引入的方法：直接引入整个文件，里面所有的类都被引入。类似 import com.*
# import HelloWorld
# 这种方式在实例化某个类时，需要完整路径：文件名.类名
# S=HelloWorld.SecondTest("唐胜凯")
# S.SayFirst()
# S.SaySecond()

# 第二种引入方法：只引入某个文件中的一个类，类似 import flash.display.Sprite
from HelloWorld import  SecondTest
# 这种方式在实例化时，不用完整路径，直接使用类名即可
ST=SecondTest("唐胜凯 "+str(0.12)) # 支持 + 号连接字符串，只是需要把其他类型强制转化为字符串
ST.SayFirst()
ST.SaySecond()

# 看来分号仍然是一行的结束符，只是省略了而已。
S1=SecondTest('Python 学习路线图'); S1.SayFirst()
S2=SecondTest('Python 学习路线图')

