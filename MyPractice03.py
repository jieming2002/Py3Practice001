__author__ = 'Skye.Tang 2017-10-29'
# 9.对象：在Python中，一切都可以看做是对象。
# Pyhon的内置对象：1数字、2字符串、3列表、4元组、5字典、6集合等等
# Pickle模块：
# 在Python中有时有一些对象需要持久性存储，并且不丢失这个对象的类型与数据，就需要将这些对象进行序列化，
# 序列化之后需要使用时，再恢复为原来的数据。这种序列化的过程，就叫pickle(腌制)。
import pickle
# 定义一个列表
listx=['one','two','three']
print(listx)
# dumps(object) 序列化
listb=pickle.dumps(listx)
print('dumps(object)序列化:{0}'.format(listb))
# loads(string)反序列化
listz=pickle.loads(listb)
print('loads(string)反序列化:{0}'.format(listz))
# dump(object,file),将对象序列化存储到文件 wb表示写二进制内容
writeFile=open('test.pke','wb') # 打开文件，没有文件就创建一个 pke=public key encryption 公开密钥加密
# 这里所用到的文件扩展名没有硬性要求，只是为了存放数据而已。另外，这种路径的文件是存放在当前项目的根目录下。
print('文件名：'+writeFile.name)
pickle.dump(listx,writeFile,True)
print(writeFile)
writeFile.close()
# load(readFile) 将dump存储在文件里的数据反序列化：rb表示读取二进制内容
readFile=open('test.pke','rb')
listTemp=pickle.load(readFile)
print('load(readFile) 将dump存储在文件里的数据反序列化：{0}'.format(listTemp))
readFile.close()

# 10.行与缩进
#物理行与逻辑行
#以下是2个物理行：每个物理行末尾默认自带一个分号，所以当一个物理行只有一个逻辑行时，末尾省略分号
print('物理行1')
print('物理行2')
# 以下是1个物理行，2个逻辑行：一行里面写两个语句，需要分号隔开
print('逻辑行1');print('逻辑行2')
# 以下是一个逻辑行，分成了多个物理行。单个语句换行。如果字符串是用 3 个引号，则换行时，不需要行连接符
print('''你说
我是
物理行，还是逻辑行？''')
# 行连接符：把多个物理行，连接一个逻辑行。一个语句分为多行。
print('我是'
      '行'\
      '连接符')
