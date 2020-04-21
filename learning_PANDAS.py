# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 01:12:16 2020

@author: Phil

"""
import pandas as pd
import numpy as np
class Lesson:
    ##定義初始化
    def __init__(self,x,y):
        self.x=x
        self.y=y
###定義實體方法
    def show(self):
        print(self.x+self.y)
    def distance(self,x,y):
        return ((self.x-x)**2+(self.y-y)**2)**0.5
        
##建立實體物件
# class Fullname:
#     def __init__(self,firtstname,lastname):
#         self.first=firtstname
#         self.last=lastname
# name1=Fullname('Chou','H.T.')
# name2=Fullname('Chen','K.G.')        

a=Lesson(30,40)        
a.show()
dis=a.distance(0,0)


aa=pd.Series([1,2,3,4])
aaa=pd.Series([1,2,3,4],index=['a','b','c','d'])
c=aaa[aaa>2]
dd=np.array([1,2,3,4])
gg=dd[dd>2]
ggg=np.exp(aaa)
adata={'a':100,'b':200,'c':300,'d':400,'e':400}
states=['california','Ohio','a','Texax','florida']
kkk=pd.Series(adata)
print(kkk)
kkkk=pd.Series(adata,index=states)
print(kkkk)
kkkkk=pd.isnull(kkkk)
###可以自動以 index 做對應運算
print(np.exp(kkk/100)+kkkk)
disct={'pop':[1,2,3,4,5],'states': ['a','s','d','f','g'] ,'year' : [2001,2002,2003,2004,2005]}

data=pd.DataFrame(disct)
print(data)
data=pd.DataFrame(disct,columns=['year','pop','states'])
print(data)

data2=pd.DataFrame(disct,index=['one','two','three','four','five'],columns=['year','pop','states'])
print(data2)
print(data2.year)
data2.loc['three']=100
print(data2)
data2.loc['pop']=100
print(data2)

###直接新增一個column 並判斷state 是否一樣
data2['y/n']=data2.states==100
print(data2)
del data2['y/n']
print(data2)
###蜂巢式結構
dictd={'kkk':{2001:1.4,2002:1.8},'ggg':{2002:2.5,2003:2.2}}
print(dictd)
frame2=pd.DataFrame(dictd)
print(frame2)
print(frame2.T)


import pandas_datareader as pdr
import datetime as datetime
import matplotlib.pyplot as plt


data = pdr.DataReader("2330.TW", "yahoo", "2000-01-01","2020-04-16")
c = data['Close']
c.plot()


df=pd.read_csv('examples/ex1.csv')
df=pd.read_csv('examples/ex1.csv',names=['a','b','c','d','messenge'])

###讀檔案 分隔號為,
df=pd.read_table('examples/ex3.csv',sep='\s+')


df=pd.read_csv('examples/ex5.csv')

df.to_csv('examples/out.csv')

import csv
class my_dialect:
    lineteminator='\n'
    delimiter=';'
    quotechar='"'
    quoting=csv.QUOTE_MINIMAL
# reader=csv.reader(f,dialect=my_dialect)    



with open('mydata.csv','w') as f:
    writer =csv.writer(f,dialect=my_dialect)
    writer.writerow(('one','two','three'))
    writer.writerow(('1','2','3'))
    writer.writerow(('1','2','3'))  
    writer.writerow(('1','2','3'))




data=pd.read_json('examples/example.json')




    






