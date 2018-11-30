#1、Numpy
#使用Numpy中loadtxt读取文本文件
import numpy as np

filename='F:/数据化运营/chapter2/numpy_data.txt'
data=np.loadtxt(filename,dtype='float32',delimiter=' ') 
print(data)

#使用Numpy的load方法读取专用的二进制文件
import numpy as np
write_data=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])   #要存储的数据
np.save('load_data',write_data)
read_data=np.load('load_data.npy')
print(read_data)

#使用Numpy中的fromfile方法读取文件
import numpy as np
filename='F:/数据化运营/chapter2/numpy_data.txt'
data=np.loadtxt(filename,dtype='float32',delimiter=' ')
tofile_name='binary'
data.tofile(tofile_name)
fromfile_data=np.fromfile(tofile_name,dtype='float32')
print(fromfile_data)

#2、pandas
#使用read_csv读取数据--read_table和read_csv是类似的
import pandas as pd
csv_data=pd.read_csv('F:/数据化运营/chapter2/csv_data.cav',names=['col1','col2'.'col3','col4','col5'])
print(data)

#使用read_fwf读取数据
import pandas as pd
f_data=pd.read_fwf('F:/数据化运营/chapter2/fwf_data',widths=[5,5,5,5])
print(f_data)

#3、xlrd
#读取excel文件
import xlrd
xlsx=xlrd.open_workbook('F:/数据化运营/chapter2/demo.xlsx')
print(xlsx.sheet_names())    #查看所有的sheet列表
print('=======================================================')
sheet1=xlsx.sheets()[0]      #获取第一张表
sheet1_name=sheet1.name      #表名称
sheet1_cols=sheet1.ncols     #总列数
sheet1_rows=sheet1.nrows     #总函数
print(sheet1_name,sheet1_cols,sheet1_rows)
#查看指定行、列数据
sheet1_row4=sheet1.row_values(4) 
sheet1_col2=sheet1.col_values(2)
#查看交叉数据，如第三行第四列 
cell23=sheet1.row_values(2)[3].value
print(sheet1_row4,sheet1_col2)
print(cell23)
print('==========================================================')
#查看每一列数据
for i in range(sheet1_rows):
    print(sheet1.row_values(i))

#4、pymysql
#使用pymysql读取数据库文件
import pymysql
db=pymysql.connect(host='localhost',user='root',password='123456',db='python_data',charset='utf8')
#获取游标
cursor=db.cursor()
try:
    sql='select * from sheet1 limit 100;'  #不要忘记写分号,写sql语句即可
    cursor.execute(sql)
    mysql_data=cursor.fetchall()       #fetchall获取查询结果
    print(mysql_data)
    cursor.close()
except:
    db.rollback()
    print('错误')                     #当存在错误操作时，回滚
finally:                               #在异常断开时，为了保证关闭数据库连接
    db.close()

#5、mongodb
#mongodb数据库的存取
from pymongo import MongoClient

client=MongoClient(host='localhost',port=27017)
datbase=client.test                 #指定数据库
collection=datbase.students          #指定集合
#插入数据
student={'id':'20181130','name':'mike','age':20,'sex':'male'}
result=collection.insert(student)     #在新的版本中使用insert_one()和insert_many()
print(result)
#查询语句
result1=collection.find_one({'id':'20181130'})
print(result1)
for i in result1:
    print(i)                   #获取所有文档数据

#6、json数据的存取
import json
json_data={'tom':{'weight':65,'score':90,'height':170}}   #字典
json_str=json.dumps(json_data)         #转化为json编码的字符串
print(type(json_str))

jsonstr_dict=json.loads(json_str)   #将字符串转为字典形式
#json.dumps,json.loads只是暂时的以json格式操作  json.dump\json.load用来存取文件

#7、读取图像数据
#一.使用PIL
from PIL import Image

imagefile='F:/数据化运营/chapter2/cat.jpg'
img=Image.open(imagefile,mode='r')
img.show()




