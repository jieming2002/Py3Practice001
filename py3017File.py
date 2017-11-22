__author__ = 'skye 2017-11-22'
# coding=utf-8

# 检索指定路径下后缀是 txt 的所有文件：
import os

# path = './data/'
def getAppointFile(path, ls):
    fileList = os.listdir(path)
    try:
        for tmp in fileList:
            pathTmp = os.path.join(path, tmp)
            print('pathTmp = ', pathTmp)
            if True == os.path.isdir(pathTmp):
                getAppointFile(pathTmp, ls)
            elif pathTmp[pathTmp.rfind('.') + 1:].upper() == 'TXT':
                ls.append(pathTmp)
    except PermissionError:
        pass

def main():
    while True:
        path = input('请输入路径：').strip()
        if os.path.isdir(path) == True:
            break
    getAppointFile(path, ls)
    print('ls = ', ls)

# 单词替换
def wordReplace(fileName, oldWord, newWord):
    path = './data/'+fileName
    fRead = open(path)
    content = []
    count = 0

    for line in fRead:
        if oldWord in line:
            count = line.count(oldWord)
            line = line.replace(oldWord, newWord)
        content.append(line)

    decide = input('''\n文件 {0} 中共有 {1} 个【{oldWord}】\n
    你确定要把所有的【{oldWord}】替换为【{newWord}】吗？\n
    【YES/NO】：'''.format(fileName, count, oldWord=oldWord, newWord=newWord))

    if decide.upper() == 'YES':
        fWrite = open(path, 'w')
        fWrite.writelines(content)
        fWrite.close()

    fRead.close()

def main2():
    fileName = input('请输入文件名：')
    oldWord = input('请输入需要替换的单词：')
    newWord = input('请输入新的单词：')
    wordReplace(fileName, oldWord, newWord)

# 函数必须先定义后调用
if __name__ == '__main__':
    ls = []
    # main()
    main2()

