# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 15:21:23 2020

@author: Phil
"""


import matplotlib.pyplot as plt
from keras.datasets import mnist
from keras.utils import np_utils


###讀取data

(train_feature,train_label),(test_feature,test_label)=mnist.load_data()

def show_images_labesls_predictions(images,labels,start_id,num=10):
    plt.gcf().set_size_inches(12,14)
    if num<25:num=25
    for i in range(num):
        ax=plt.subplot(5,5,i+1)
        ax.imshow(images[start_id],cmap='binary')
        title='label='+str(labels[start_id])
        ax.set_title(title,fontsize=12)
        ax.set_xticks([]);ax.set_yticks([])
        start_id+=1
    plt.show()
show_images_labesls_predictions(train_feature,train_label,0,10)
 
###reshpe後轉成一維 並normalize       
train_feature_normalize=train_feature.reshape(len(train_feature),784).astype('float32')/255
print(train_feature_normalize[0])
###轉成 one hot encoding 為了讓計算更有效率
train_label_onehot=np_utils.to_categorical(train_label)
print(train_label_onehot[0:5])

###built learning model
from keras.models import Sequential
from keras.layers import Dense

model=Sequential()
###輸入層(units 隱藏層神經原數目  input 輸入層神經原數目 normal 常態分佈的亂數初始化權重  激勵函式為relu)
model.add(Dense(units=256,input_dim=784,kernel_initializer='normal',activation='relu'))
###輸出層(units 輸出層神經原數目 沒有輸入層 激勵函式為softmax
model.add(Dense(units=10,kernel_initializer='normal',activation='softmax')) 
###模型的訓練方式(定義損失函數 最佳化方法 評估準確率方法)
model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
###進行訓練(x=特徵值,y=標記值,validation_split=驗證資料百分比,epochs=訓練次數,verbose=是否顯示訓練過程)
model.fit(x=train_feature_normalize,y=train_label_onehot,validation_split=0.2,epochs=200,verbose=2)


model.save('Machine_learning23.3.6.h5')
from keras.datasets import mnist
import matplotlib.pyplot as plt
from keras.models import load_model

def show_images_labels_predictions(images,labels,predictions,start_id,num=10):
    plt.gcf().set_size_inches(12, 14)
    if num>25: num=25 
    for i in range(0, num):
        ax=plt.subplot(5,5, i+1)
        ax.imshow(images[start_id], cmap='binary')  #顯示黑白圖片
        if( len(predictions) > 0 ) :  #有傳入預測資料
            title = 'ai = ' + str(predictions[start_id])
            # 預測正確顯示(o), 錯誤顯示(x)
            title += (' (o)' if predictions[start_id]==labels[start_id] else ' (x)') 
            title += '\nlabel = ' + str(labels[start_id])
        else :  #沒有傳入預測資料
            title = 'label = ' + str(labels[start_id])
        ax.set_title(title,fontsize=12)  #X,Y軸不顯示刻度
        ax.set_xticks([]);ax.set_yticks([])        
        start_id+=1 
    plt.show()

(train_feature, train_label), (test_feature, test_label) = mnist.load_data()
test_feature_vector = test_feature.reshape(len( test_feature), 784).astype('float32')
test_feature_normalize = test_feature_vector/255
model = load_model('Machine_learning23.3.6.h5')

prediction=model.predict_classes(test_feature_normalize)  #預測
show_images_labels_predictions(test_feature,test_label,prediction,0)


###使用自製的圖片 做預測
import cv2 as cv
import glob as glob
import numpy as np
from keras.models import load_model
files=glob.glob("imagedata\*.jpg")
test_feature=[]
test_label=[]

for file in files :
    # file=files[0]
    img=cv.imread(file)
    img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)              ###RGB轉灰階
    _,img=cv.threshold(img,120,255,cv.THRESH_BINARY_INV)###(image,threshold,max value,type)
    test_feature.append(img)                            ###疊成10張圖
    test_label.append(file[10:11])                      ###
    
test_feature=np.array(test_feature)                     ###transform to array
test_label=np.array(test_label)                         ###transform to array

###arrange to 10 vector and normalize
test_feature_vector=test_feature.reshape(len(test_feature),784).astype('float32')/255    
    
### load model    
model = load_model('Machine_learning23.3.6.h5')    

### predict
prediction=model.predict_classes(test_feature_vector)
 ### show image and predict result   
show_images_labels_predictions(test_feature,test_label,prediction,0,len(test_feature))    
    





