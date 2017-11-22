__author__ = 'skye 2017-11-22'
# coding=utf-8

import os

def searchFile(startDir, target):
    os.chdir(startDir)

    for file in os.listdir(os.curdir):
        ext = os.path.splitext(file)[1]
        if ext in target:
            fileList.append(os.getcwd() + os.sep + file + os.linesep)
        if os.path.isdir(file):
            searchFile(file, target)    # 递归调用
            os.chdir(os.pardir)         # 递归调用后切记返回上一层目录

startDir = input('请输入待查找的初始目录：')
workDir = os.getcwd() #当前工作目录

target = ['.txt', '.jpg', '.pkl', '.png']
fileList = []
searchFile(startDir, target)

f = open(workDir + os.sep + 'data' + os.sep + 'fileList.txt', 'w')
f.writelines(fileList)
f.close()

