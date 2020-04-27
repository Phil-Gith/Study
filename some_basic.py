# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 10:39:23 2020

@author: Phil
"""

###except 可以捕捉所有例外 包括所有的系統例外
try:
    print(n)
except:
    print("變數 n 不存在啦")

try:
    print(n)
except Exception as e:
    print(e)

try:
    a=int(input("a="))
    b=int(input("b="))
    r=a % b
except(ValueError,ZeroDivisionError) as e:
        print("發生 {} 錯誤!".format(e))
else:
    print("r=",r)


### raise(例外類型) 新增一個自定義的例外類型
def checkspeed(speed):
    if speed<70:
        raise Exception("烏龜呀!!!")
    elif speed>110:
        raise Exception("優~ 很快優")

for speed in range(50,150,10):
    print(speed)
    try:
        checkspeed(speed)
    except Exception as e:
        print("現在速度{}:{}".format(e,Exception))





name='Fiona'
score=80

#   % 參數格式化
#   %5d 固定列印五字元 少於五位數 會填入空白 
#   %5s 固定列印五字元 少於五個字元 會填入空白
#   %8.2f 列印8個字元的浮點數小數點下兩位 少於兩位變0 
 
print("%s 的成績為 %d" %(name,score))

print("{} 的成績為 {}".format(name,score))


#  input([提示字串])
a=int(input('A='))
b=int(input('B='))
print("A+B=",a+b)
dict1={"A":"內向穩重","B":"外向樂觀","O":"堅強自信","AB":"聰明自然"}
a=input("請輸入血型:")

if a=="A":
    print(dict1["A"])
elif a=="B":
    print(dict1["B"])
elif a=="O":
    print(dict1["O"])
elif a=="AB":
    print(dict1["AB"])
else:
    print("沒這種血型喔")
if a in dict1:
    print("{}血型的個性為{}".format(a,dict1[a]))
else:
    print("沒這種血型喔")

list1=list(dict1.keys())
list2=list(dict1.values())
for i in range(len(dict1)):
    print("{}血型個性為{}".format(list1[i],list2[i]))


cc=dict1.items()
print(dict1.items())


