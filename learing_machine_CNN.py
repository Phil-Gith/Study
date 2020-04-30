# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 11:08:06 2020

@author: Phil
"""

from keras.datasets import mnist
from keras.utils import np_utils


(train_feature,train_label),(test_feature,test_label)=mnist.load_data()
train_feature_normalize=train_feature.reshape(len(train_feature),28,28,1).astype('float32')/255

test_feature_normalize = test_feature.reshape(len( test_feature),28,28,1).astype('float32')/255
train_label_onehot=np_utils.to_categorical(train_label)
test_label_onehot=np_utils.to_categorical(test_label)

from keras.models import Sequential
from keras.layers import Conv2D,MaxPooling2D,Dense,Flatten

model= Sequential()

###build convolution layer
###(filters=10,kernel_size=(3,3),padding='same'            ,input_shape=(28,28,1),activation='relu')
### 10 filters   filter size     set convolution image size  input size              激勵函數???    
model.add(Conv2D(filters=10,kernel_size=(5,5),padding='same',input_shape=(28,28,1),activation='relu'))

###build pooling layer
###10 28*28 image to get 10 14*14(長寬皆除以2)
model.add(MaxPooling2D(pool_size=(2,2)))

###build second convolution layer
###似乎不需再設定 input image size
model.add(Conv2D(filters=20,kernel_size=(5,5),padding='same',activation='relu'))


###build second pooling layer
###20 14*14 image to get 20 7*7(長寬皆除以2)
model.add(MaxPooling2D(pool_size=(2,2)))

###build flaten layer
###將20張7*7 圖片轉換成20*7*7的一維向量
model.add(Flatten())

###建立隱藏層
model.add(Dense(units=256,activation='relu'))

###建立輸出層
model.add(Dense(units=10,activation='softmax'))

model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
model.fit(x=train_feature_normalize,y=train_label_onehot,validation_split=0.2,epochs=10,batch_size=200,verbose=2)

scores=model.evaluate(test_feature_normalize,test_label_onehot)
model.save('Mnist_cnn_model.h5')


import cv2 as cv
import glob as glob
import numpy as np
from keras.models import load_model
import matplotlib.pyplot as plt
files=glob.glob("imagedata\*.jpg")
test_feature=[]
test_label=[]

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



for file in files :
    # file=files[0]
    img=cv.imread(file)
    img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)              ###RGB轉灰階
    _,img=cv.threshold(img,120,255,cv.THRESH_BINARY_INV)###(image,threshold,max value,type)
    test_feature.append(img)                            ###疊成10張圖
    test_label.append(file[10:11])                      ###
    
test_feature=np.array(test_feature)                     ###transform to array
test_label=np.array(test_label)                         ###transform to array

test_feature_vector=test_feature.reshape(len(test_feature),28,28,1).astype('float32')/255

model=load_model('Mnist_cnn_model.h5')
prediction=model.predict_classes(test_feature_vector)
show_images_labels_predictions(test_feature,test_label,prediction,0,len(test_feature))   



