# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 12:49:04 2020

@author: Phil
"""
import os
import sqlite3 as SQ
conn=SQ.connect("mydata.db")                ###連結資料夾or建立資料夾
conn.close()                                ###操作結束


###建立學生表單

conn=SQ.connect("data11_2.db")
cursor=conn.cursor()                        ###建立 cursor 物件 像是游標在 料庫裡移動

sql='''create table student(id int,
                            name text,
                            gender text)''' ###建立student 表單 分別為ID(int) name(str) gender(str) 
# cursor.execute(sql)
cursor.close()
conn.close()


###建立之後使用範例
conn=SQ.connect("myinfo.db")
seq='''create table student(id int,name text,gender text)'''
# conn.execute(seq)

conn.close()

###ex11_4 依序輸入入建立表單
conn=SQ.connect("myinfo.db")
print("Please input student info:")
while True:
    new_id=int(input("please input student id:"))
    new_name=str(input("please input student name:"))
    new_gender=str(input("please input student gender:"))
    x=(new_id,new_name,new_gender)
    sql='''insert into student values(?,?,?)'''
    conn.execute(sql,x)
    conn.commit()
    again=input("more info to input(y/n)?")
    if again=='n':
        break    
conn.close()
    
###建立之後使用範例
conn=SQ.connect("myinfo2.db")
seq='''create table student2(id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name text,
                            gender text)'''### ID 新增的方式 是用 自動增值不需輸入
# conn.execute(seq)

conn.close()


###ex11_4_1 依序輸入入建立表單
conn=SQ.connect("myinfo2.db")
print("Please input student info:")
while True:
    new_name=str(input("please input student name:"))
    new_gender=str(input("please input student gender:"))
    x=(new_name,new_gender)
    sql='''insert into student2(name,gender) values(?,?)'''
    conn.execute(sql,x)
    conn.commit()
    again=input("more info to input(y/n)?")
    if again=='n':
        break    
conn.close()


###查詢資料表
conn=SQ.connect("myinfo.db")
data=conn.execute("SELECT * from student")
students=data.fetchall()                    ###從資料夾抓出來 資料庫關閉後可以繼續使用
data1=conn.execute("SELECT name from student")
student_name=data1.fetchall()
#### SELECT 欄位
#### from 表單
#### where 條件

data2=conn.execute('''SELECT name, gender from student where gender="female"''')
student_name_genderfilter=data2.fetchall()
for i in data:
    print(i[0],i[1],i[2])
    print(i)
print("-------------------------")
for i in students:
    print(i)
print("-------------------------")
for i in student_name:
    print(i)
print("-------------------------")
for i in student_name_genderfilter:
    print(i)
conn.close()

###更新資料庫
conn=SQ.connect("myinfo.db")
sql='''UPDATE student set name = "Tony" where id=1'''
conn.execute(sql)
conn.commit()
#### UPDATE 表單
#### set 欄位 新內容
#### where 標記哪一筆紀錄
result=conn.execute('''SELECT name from student ''')
data=result.fetchall()
print(data)
conn.close()

###刪除資料庫 一項內容
conn=SQ.connect("myinfo.db")
sql='''DELETE from student where id=1'''
conn.execute(sql)
conn.commit()

result=conn.execute('''SELECT name from student ''')
data=result.fetchall()
print(data)
conn.close()

conn=SQ.connect("myinfo.db")
new_id=int(input("please input student id:"))
new_name=str(input("please input student name:"))
new_gender=str(input("please input student gender:"))
x=(new_id,new_name,new_gender)
sql='''insert into student values(?,?,?)'''
conn.execute(sql,x)
conn.commit()

result=conn.execute('''SELECT * from student ''')
data=result.fetchall()
print(data)
conn.close()

####ch11_11 專題 將csv 檔變成 資料庫\
import csv
import matplotlib.pyplot as plt
import sqlite3 as SQ

with open('Taipei_Population.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    data= list(csv.reader(csvfile))
    title=data[1:4]
    data=data[4:]
    
###建立資料庫和表格
conn=SQ.connect("data11_11_2.db")
title[0][0]
conn.execute('''DROP TABLE population''')
sql='''create table population(area text,
                            population int,
                            male int,
                            female int)'''
conn.execute(sql)
for a in data:
    x=(a[0],int(a[6]),int(a[7]),int(a[8]))
    print(x)
    sql='''insert into population values(?,?,?,?)'''
    conn.execute(sql,x)
conn.commit()

conn=SQ.connect("data11_11_2.db")
result=conn.execute('''SELECT * from population ''')
data=result.fetchall()

print(data)

area,male,female,total=[],[],[],[]
for i in data:
    print(i)
    area.append(i[0])
    male.append(i[2])
    female.append(i[3])
    total.append(i[1])

###畫出多個一維線圖
# 將字體換成SimHei
plt.rcParams['font.sans-serif'] = ['SimHei']
# 修復負號顯示問題
plt.rcParams['axes.unicode_minus']=False


plt.plot(area,total,marker='o',label='total')
plt.plot(area,male,marker='o',label='male')
plt.plot(area,female,marker='^',label='female')
.xticks(area)

# figure()
plt.plot(area,female,label='female',markde='o')

conn.close()

import matplotlib
# 將字體換成SimHei
plt.rcParams['font.sans-serif'] = ['SimHei']
# 修復負號顯示問題
plt.rcParams['axes.unicode_minus']=False
plt.rcParams['font.sans-serif'] = ['Noto Sans CJK TC']
x_labels = ['小', '中', '大']
x = range(len(x_labels))
y = [-3, 0, 3]

plt.scatter(x, y)
plt.xticks(x,x_labels)
plt.tick_params(axis='x', which='major', labelsize=30)

plt.show()