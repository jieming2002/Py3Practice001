__author__ = 'skye2017-11-18'
# coding=utf-8
# 在Python中没有switch – case语句。

a = 100
if a:
    print('1 - if 表达式条件为 true')
    print(a)

b = 0
if b: # 布尔值除了 0 都是 true
    print('2 - if 表达式条件为 true')
    print(b)
print('再见')

age = int(input('请输入你家狗狗的年龄: '))
print('回答：', end='')
if age < 0:
    print('你是在逗我吧!')
elif age == 1:
    print('相当于 14 岁的人。')
elif age == 2:
    print("相当于 22 岁的人。")
elif age > 2:
    human = 22 + (age - 2) * 5
    print('对应人类年龄: ', human)
input('点击 enter 键退出')

# 该实例演示了数字猜谜游戏
num = 7
guess = -1
print('数字猜谜游戏!')
while guess != num:
    guess = int(input('请输入你猜的数字：'))

    if guess == num:
        print('恭喜，你猜对了！')
    elif guess < num:
        print('猜的数字小了...')
    elif guess > num:
        print('猜的数字大了...')

# 以下实例 x 为 0-99 取一个数,y 为 0-199 取一个数,
# 如果 x>y 则输出 x， 如果 x 等于 y 则输出 x+y，否则输出y。
import random

x = random.choice(range(100))
y = random.choice(range(200))

if x > y:
    print('x:',x)
elif x == y:
    print('x+y:', x+y)
else:
    print('y:',y)

"""对上面例子的一个扩展"""
print("=======欢迎进入狗狗年龄对比系统========")
while True:
    try:
        age = int(input("请输入您家狗的年龄:"))
        print("回答：", end='')
        age = float(age)
        if age < 0:
            print("您在逗我？")
        elif age == 1:
            print("相当于人类14岁")
            break
        elif age == 2:
            print("相当于人类22岁")
            break
        else:
            human = 22 + (age - 2)*5
            print("相当于人类：",human)
            break
    except ValueError:
        print("输入不合法，请输入有效年龄")
###退出提示
input("点击 enter 键退出")

