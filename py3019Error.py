__author__ = 'skye 2017-11-22'
# coding=utf-8

import sys
import os

def inputInt():
    while True:
        try:
            x = int(input('请输入一个整数：'))
            break
        except ValueError:
            print('靠，你输入的不是整数，重新输：')
        # 一个except子句可以同时处理多个异常
        except (RuntimeError, TypeError, NameError):
            pass
        # 最后一个except子句可以忽略异常的名称，它将被当作通配符使用。
        except:
            print("Unexpected error:")
            raise

    print('对啦，你输入的整数是：', x)

def errorHandler():
    try:
        f = open('./data/test.jpg')
        s = f.readline()
        i = int(s.strip())
    except OSError as err:
        print('操作系统错误：', err)
    except ValueError:
        print('无法把数据转换为整数')
    # 最后一个except子句可以忽略异常的名称，它将被当作通配符使用。
    except:
        print('报错啦：', sys.exc_info()[0])
        raise  #使用 raise 语句抛出一个异常

def useElseInTry(data_dir):
    '''try except 语句还有一个可选的 else 子句，
    如果使用这个子句，那么必须放在所有的 except 子句之后。
    这个子句将在 try 子句没有发生任何异常的时候执行。

    使用 else 子句比把所有的语句都放在 try 子句里面要好，
    这样可以避免一些意想不到的、而 except 又没有捕获的异常。
    '''
    fileList = os.listdir(data_dir)
    for fName in fileList:
        try:
            f = open(data_dir + fName, 'r')
        except IOError:
            print('无法打开 ', fName)
        else:
            try:
                print(fName, ' 有 ', len(f.readlines()), ' 行')
                f.close()
            except:
                print(fName, '报错啦：', sys.exc_info()[0])

def raiseError():
    '''使用 raise 语句抛出一个指定的异常。
    raise 唯一的一个参数指定了要被抛出的异常。它必须是一个异常的实例。
    '''
    try:
        raise NameError('自己抛出的异常：名称错误')
    except NameError:
        print('报错啦')
        raise #再次抛出这个异常

'''你可以通过创建一个新的 exception 类来拥有自己的异常。
异常应该继承自 Exception 类，或者直接继承，或者间接继承
'''
class MyError(Exception):
    def __init__(self, value):  #构造函数？
        self.value = value
    def __str__(self):
        return repr(self.value)

def raiseMyError():
    try:
        raise MyError(2*2)
    except MyError as e:
        print('我自定义的异常，编号 = ', e.value)

def devide(x, y):
    ''' 不管 try 子句里面有没有发生异常，finally 子句都会执行。
    如果一个异常在 try 子句里（或者在 except 和 else 子句里）被抛出，
    而又没有任何的 except 把它截住，那么这个异常会在 finally 子句执行后再次被抛出。
    '''
    try:
        result = x / y
    except ZeroDivisionError:
        print('除数不能是 0')
    else:
        print('计算结果：', result)
    finally:
        print('执行 finally 语句')

def sysClear():
    ''' 预定义的清理行为
    一些对象定义了标准的清理行为，无论系统是否成功的使用了它，一旦不需要它了，那么这个标准的清理行为就会执行。
    '''
    for line in open('./data/test.txt'):
        print(line, end='')
    # 以上这段代码的问题是，当执行完毕后，文件会保持打开状态，并没有被关闭。
    # 关键词 with 语句就可以保证诸如文件之类的对象在使用完之后一定会正确的执行他的清理方法:
    print('\r\n')
    with open('./data/test.txt') as f:
        for line in f:
            print(line, end='')
    # 以上这段代码执行完毕后，就算在处理过程中出问题了，文件 f 总是会关闭。

if __name__ == '__main__':
    # inputInt()
    # errorHandler()
    # useElseInTry('./data/')
    # raiseError()
    # raiseMyError()
    # devide(1, 2)
    # devide(2, 0)
    # devide('a', 'b')
    sysClear()


