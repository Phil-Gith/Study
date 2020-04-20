# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 17:40:56 2020

@author: Phil
"""

import json
list_n=[1,2,3,4]
tuple_n=(5,6,7,8)
jsondata1=json.dumps(list_n)
jsondata2=json.dumps(tuple_n)
##轉 json file 後 便str
print(jsondata1, type(jsondata2))
print(jsondata2, type(jsondata2))

dictobj={'simon':10,'trisa':20,'cloud':236}

jsondata3=json.dumps(dictobj)
print(jsondata3, type(jsondata3))

players = {'Stephen Curry':'Golden State Warriors',
           'Kevin Durant':'Golden State Warriors',
           'Lebron James':'Cleveland Cavaliers',
           'James Harden':'Houston Rockets',
           'Paul Gasol':'San Antonio Spurs',
          }
jsondata4=json.dumps(players,sort_keys=True)
jsondata5=json.dumps(players,sort_keys=False)

print(jsondata4, type(jsondata4))
print('排序是否相同:',jsondata4==jsondata5)

jsondata5=json.dumps(players,sort_keys=True,indent=4)

print(jsondata5, type(jsondata5))


###轉為 python 物件 使用 loads

json_obj='{"aa":10,"b":20,"c":30}'
dictobj=json.loads(json_obj)
print(dictobj, type(dictobj))


###json 只能放一哥物件 有兩個時要放在 dict 裡


# obj='{"asia":{"Tokyo":100,"taypei":10000}}'
# jsondata=json.dumps(obj)
# print(jsondata,type(jsondata))
# print(jsondata[0])
# print(jsondata['asia'][0])
# print(jsondata['asia'][1]['Tokyo'])
# print(jsondata['asia'][1]['taypey'])

# ch1_6.py
import json

obj = '{"Asia":[{"Japan":"Tokyo"},{"China":"Beijing"}]}'
json_obj = json.loads(obj)
print(json_obj)
print(json_obj["Asia"])
print(json_obj["Asia"][0])
print(json_obj["Asia"][1])
print(json_obj["Asia"][0]["Japan"])
print(json_obj["Asia"][1]["China"])


       
dictObj = {'b':80, 'a':25, 'c':60}   
with open('out1_8.json','w') as kkk:
    json.dump(dictObj,kkk,indent=4)

with open('out1_8-1.json','w') as kkk:
    json.dump(players,kkk,indent=4)

objdict2=[{"國家":"日本","首都":"東京","鄉下":"北海道"},{"國家":"台灣","首都":"台北","鄉下":"花蓮"}]

with open('out1_9-1.json','w',encoding='utf-8') as kkk:
    json.dump(objdict2,kkk,indent=4,ensure_ascii=False)

with open('out1_9-1.json','r',encoding='utf-8') as kkk:
   data=json.load(kkk)
print(data, type(data))



#####專題
from pygal.maps.world import COUNTRIES
with open('D:\\Study Project\\Web_Crawler\\ch1\\populations.json','r',encoding='utf-8') as kkk:
    data=json.load(kkk)

for i in range(len(data)):
    print(data[i]['Country Code'],'   ',data[i]['Country Name'])
for countrycode in sorted(COUNTRIES.keys()):
    print(countrycode,'  ',COUNTRIES[countrycode])

def getCountryCode(A):
    # A='China'
    for code,name in COUNTRIES.items():
        # print(name,code)
        if A == name:
            return code
    return None
    
code=getCountryCode('China')

for i in range(len(data)):
    code=getCountryCode(data[i]['Country Name'])
    if code==None:
        print('名稱不吻合')
    else:
        print(data[i]['Country Name'],int(data[i]['Numbers']),data[i]['Year'],'  ',code)

import pygal.maps.world        
worldmap=pygal.maps.world.World()
worldmap.title='China/Japan/Thailand'
worldmap.add('China',['cn','jp','th'])
worldmap.render_to_file('worldmap_2.svg')

import pygal.maps.world        
worldmap=pygal.maps.world.World()
worldmap.title='China/Japan/Thailand'
worldmap.add('Asia',{'cn':123456,'jp':654328,'th':85698})
worldmap.render_to_file('worldmap_3.svg')

dictdata={}
for getdata in data:
    # print(getdata)
    if getdata['Year']=='2000':
        code=getCountryCode(getdata['Country Name'])
        dictdata[code]=float(getdata['Numbers'])
        if code==None:
            print('名稱不吻合')
        else:
            print(getdata['Country Name'],getdata['Numbers'],code,getdata['Country Code'])

worldmap=pygal.maps.world.World()
worldmap.title='World population in 2000'
worldmap.add('2000 Year',dictdata)
worldmap.render_to_file('worldmap_4.svg')



dictdata={}
for getdata in data:
    # print(getdata)
    if float(getdata['Numbers'])>100000000:
        code=getCountryCode(getdata['Country Name'])
        dictdata[code]=float(getdata['Numbers'])
        if code==None:
            print('名稱不吻合')
        else:
            print(getdata['Country Name'],getdata['Numbers'],code,getdata['Country Code'])

worldmap=pygal.maps.world.World()
worldmap.title='World population > 100M'
worldmap.add('2000 Year',dictdata)
worldmap.render_to_file('worldmap_5.svg')





