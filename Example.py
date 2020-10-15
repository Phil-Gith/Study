# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 13:44:51 2019

@author: PhilChou
"""
###使用matplotlib 去監控即時動態的影像
plt.ion()  #開啟一個互動視窗
plt.rcParams['figure.figsize'] = (10, 10)          # 图像显示大小
plt.rcParams['font.sans-serif']=['SimHei']        #防止中文标签乱码，还有通过导入字体文件的方法
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['lines.linewidth'] = 0.5               #设置曲线线条宽度
###開始進入迴圈即時監控顯示
plt.clf()                                             #清除刷新前的图表，防止数据量过大消耗内存
plt.suptitle("For alignment",fontsize=30)             #添加总标题，并设置文字大小
#图表1
agraphic=plt.subplot(2,1,1)
agraphic.set_title('X-profile')                       #添加子标题
agraphic.set_xlabel('pixel(x-direction)',fontsize=10)   #添加轴标签
agraphic.set_ylabel('confidence', fontsize=10)
plt.axvline(80, color= 'k')                            #畫垂直線  
plt.plot(conf[30,:],'g-')                              #等于agraghic.plot(ax,ay,'g-')
#图表2
bgraghic=plt.subplot(2, 1, 2)
bgraghic.set_title('Y-profile')
bgraghic.set_xlabel('pixel(y-direction)',fontsize=10)   #添加轴标签
bgraghic.set_ylabel('confidence', fontsize=10)
plt.axvline(30, color= 'k')                             #畫垂直線
plt.plot(conf[:,80],'r-')

###存成 open CV 格式

path="D:\\IT1\\1007\\NO3_epc635_2ms\\epc635_#3_LUT.xml"
s = cv2.FileStorage()
s.open(path, cv2.FileStorage_WRITE)
s.write('Phase_1000mm' ,phase_all[1])
s.write('LUT',Lut)
s.release()



#example
#畫圖
###https://ithelp.ithome.com.tw/articles/10201670
###https://blog.csdn.net/claroja/article/details/70841382
fig,ax=plt.subplots(3,2)
fig, ax = plt.subplots(3,12)  
for i in range(PhaseAve.shape[2]-1):
    im=ax[0,i].imshow(PhaseAve[:,:,i],vmin=500,vmax=3500,cmap='jet')
    ax[0,i].set_title(index[i],fontsize=8)
    ###劃出colorbar 並定義其大小(fraction) 邊距(pad) 水平的bar
    ax1=plt.colorbar(im,fraction=0.4, pad=0.04,orientation="horizontal",ax=ax[0,i])
    ax[0,i].set_xticks([])
    ax[0,i].set_yticks([])
    

im=ax[1,0].imshow(PhaseAve[:,:,3],label='20M phase',cmap='jet',vmin=0,vmax=900)
plt.colorbar(im,ax=ax[1,0])
ax[1,0].set(xlim=[0,79],ylim=[0,59],title="20M phase",xlabel="Pixels",ylabel="Pixels")
im=ax[1,1].imshow(PhaseAve[:,:,2],label='40M phase',cmap='jet',vmin=0,vmax=900)
plt.colorbar(im,ax=ax[1,1])
ax[1,1].set(xlim=[0,79],ylim=[0,59],title="40M phase",xlabel="Pixels",ylabel="Pixels")
plt.subplots_adjust(wspace =0.5, hspace =0.5)

delta=PhaseAve[:,:,3]-mainPhase

im=ax[2,0].imshow(delta,label='delta',cmap='jet',vmin=-40,vmax=40)
plt.colorbar(im,ax=ax[2,0])
ax[2,0].set(xlim=[0,79],ylim=[0,59],title="delta",xlabel="Pixels",ylabel="Pixels")
im=ax[2,1].imshow(delta+PhaseAve[:,:,3],label='delta+20M',cmap='jet',vmin=0,vmax=500)
plt.colorbar(im,ax=ax[2,1])
ax[2,1].set(xlim=[0,79],ylim=[0,59],title="delta+20M",xlabel="Pixels",ylabel="Pixels")

plt.subplots_adjust(wspace =0.5, hspace =0.5)

fig,ax=plt.subplots(1,1)
A0=np.linspace(174,474,4)
ax.plot(A0,DepthCenter,marker='o',label='Multipath effect')
ax.plot(A0,A0,marker='o',label='Real')
ax.plot(A0,a(A0),marker='^',label='Fit')
ax.plot(A0,(DepthCenter-measuredFit[1])/measuredFit[0],marker='o',label='Calibrated')
ax.text(A0[2]+20, DepthCenter[2],'y='+str(round( measuredFit[0],2))+'x'+ str(round( measuredFit[1],2)))
#
ax.set(xlim=[130,500],ylim=[130,700],title="GT2 multipath effect",ylabel="depth",xlabel="real distance(mm)")
ax.legend()

##設定座標軸
plt.ticklabel_format(style='sci', axis='x',  scilimits=(0,3))##設定座標軸X為科學記號



str(round( measuredFit[0],2)

###畫bar error bar 圖 

fig, ax = plt.subplots() 
# Draw bars, position them in the center of the tick mark on the x-axis 
ax.bar(index, uniformity_mean, color = '#008B8B', align = 'center',edgecolor='k',width=0.6,linewidth=1.5) 
# Draw error bars to show standard deviation, set ls to 'none' 
# to remove line between points 
ax.errorbar(index, uniformity_mean, yerr = uniformity_std, color = 'k', fmt='o', markersize=3, capsize=2) 
ax.set_ylabel('uniformity',fontsize=16) 
ax.set_xlabel("sample",fontsize=16)
ax.set_xticks(index, minor=False)
plt.xticks(rotation=335)
# ax.xticks() 
ax.set_title('Uniformity',fontsize=18)  
# ax.spines['bottom'].set_linewidth(bwith)
# ax.spines['left'].set_linewidth(bwith)
# ax.spines['top'].set_linewidth(bwith)
# ax.spines['right'].set_linewidth(bwith)


###畫bar error bar 圖     
fig, ax = plt.subplots() 
# Draw bars, position them in the center of the tick mark on the x-axis 
ax.bar(index, mean, color = '#539caf', align = 'center',edgecolor='k', width=0.5,linewidth=2) 
# Draw error bars to show standard deviation, set ls to 'none' 
# to remove line between points 
ax.errorbar(index, mean, yerr = STD, color = '#297083', fmt='o', markersize=3, capsize=2) 
ax.set_ylabel('Accuracy average',fontsize=16) 
ax.set_xlabel("Material",fontsize=16)
ax.set_xticks(index, minor=False)
plt.xticks(rotation=335)
# ax.xticks() 
ax.set_title('Material effect in L515',fontsize=18)  
    
    
###畫3D 圖      
fig = plt.figure()
ax  = fig.add_subplot(111, projection='3d')
ax.scatter(points[:,0],points[:,1],points[:,2],color='b')
ax.scatter(iin[:,0],iin[:,1],iin[:,2], color='r')
ax.scatter(oout[:,0],oout[:,1],oout[:,2],color='g')
# ax.plot_surface(x, y, z(x,y))
ax.view_init(10, 60)    
xlim = ax.get_xlim()
ylim = ax.get_ylim()
X,Y = np.meshgrid(np.arange(xlim[0], xlim[1]),
                  np.arange(ylim[0], ylim[1]))
Z = np.zeros(X.shape)
for r in range(X.shape[0]):
    for c in range(X.shape[1]):
        Z[r,c] = best_fit_box[0] * X[r,c] + best_fit_box[1] * Y[r,c] + best_fit_box[2]
ax.plot_wireframe(X,Y,Z, color='#E6E6FA')
plt.show()

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()  
    
    
    
#16bit 圖檔讀圖
UndistortPhase[:,:,a]=cv2.imread(filepath[j],-1)


###存PGM檔
LipsDepth501=LipsDepth50.astype('int')
LipsDepth502=np.uint16(LipsDepth50)
np.fromfile('D:\\HT3_0305\\HT3 image\\HT3_0305_depth_np.pgm',LipsDepth501)
cv2.imwrite('D:\\HT3_0305\\HT3 image\\HT3_0305_depth.pgm',LipsDepth502)

###csvwrite


from csv import writer
with open('D:\\pixelscope_data\\'+args.arg5+'.csv', 'w', newline='') as csvfile:
  # 建立 CSV 檔寫入器
  writer = writer(csvfile)
  for i in range(len(Time)):
      writer.writerow([Time[i],Volts[i],IT1Time[i],IT1Volts[i]])

import csv
with open('remap_X.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        remapX= list(csv.reader(csvfile))####轉t成 numpy array 的形式
        for row in spamreader:
            
            print(', '.join(row))
            
####file summary
from os import listdir
from os.path import isfile, isdir, join
from os import walk
    mypath= path
    A=listdir(mypath)
    A.sort(key= lambda x:int(x[4 :]))  
    B=listdir(mypath)
    B.sort(key= lambda x:int(x[4 :]))
    for i in range(len(A)):
        A[i]=mypath+"\\"+A[i]
        B[i]=int(B[i].strip("DLL_"))
        
#####OPEN CV 專用檔案格式讀取方式

# path="D:\\IT1\\20200810test\\1500LJ2200004.xml_IT1.xml"
s = cv2.FileStorage()
s.open(path, cv2.FileStorage_READ)
###讀取array時
P2 = (s.getNode('P2')).mat()
P1 = (s.getNode('P1')).mat()
cameramatrix=(s.getNode('cameraMatrixTOF')).mat()
lookUptable=(s.getNode('P_LUT')).mat()
DLL_delay=(s.getNode('phaseOffset1')).real()
###讀取string時
product_sn=(s.getNode('product_sn')).string()
###讀取單一數值時
modulationFrequency1=(s.getNode('modulationFrequency1')).real()


#####從CSV檔直接讀成 numpy array 
my_data = genfromtxt('D:\\pixelscope_data\\pixelscope_data\\'+B[i], delimiter=',')
#####從matrix 輸出成 csv 
np.savetxt('D:\\GT1 flying pixel\\end\\GT1\\GT1depth_hands_filt.csv', GT1depth_hands_filt, delimiter = ',')


####Fourieer transform waveprofile 轉 頻率空間 在一維
N = 9952                    # the number of points
Fs = 1/2/10**(-10)          # the sampling rate(一秒取幾個點)
Ts = 1/Fs                   # the sampling period
freqStep = Fs/N             # resolution of the frequency in frequency domain
freq = freqStep * np.arange(-N/2, N/2)
t = np.arange(N)*Ts         # x ticks in time domain, t = n*Ts
y = average[:,3]            # Signal to analyze
Y = np.fft.fft(y)           # Spectrum
Y = np.fft.fftshift(Y)      # middles the zero-point's axis

aaaa=np.argsort(Y)
bbbb=freq[aaaa]
fig,ax=plt.subplots(1,2)
ax[0].plot(average[:,2],average[:,3],label='Time domain')
ax[0].set(title="Singal in Time domain",xlabel="time(S)",ylabel="Volt(mV)")
ax[0].legend()
ax[1].plot(freq, abs(Y)/N,label='Frequency domain')
ax[1].set(title="Singal in Frequency domain",xlabel="frequency",ylabel="Magnitude (Linear)'")
ax[1].legend()



###使用多項式fitting

reg=np.polyfit(c,time,1) ##輸入 x,y 用一次式找出方程式 x=c y=time
c=np.linspace(0,128*(int(len(A))-1),int(len(A))) 
ry=np.polyval(reg,c)###使用方程式套入x=c 來算出方程式的值

#來計算 r-squared
p = np.poly1d(reg)
# fit values, and mean
yhat = p(c)                         # or [p(z) for z in x]
ybar = np.sum(time)/len(time)          # or sum(y)/len(y) 平均值
ssreg = np.sum((yhat-ybar)**2)   # or sum([ (yihat - ybar)**2 for yihat in yhat])
sstot = np.sum((time - ybar)**2)    # or sum([ (yi - ybar)**2 for yi in y])
Rsuqare = ssreg / sstot


#### 內插

import numpy as np
from scipy import interpolate
import pylab as pl
 
x=np.linspace(0,10,11)
#x=[  0.   1.   2.   3.   4.   5.   6.   7.   8.   9.  10.]
y=np.sin(x)
xnew=np.linspace(0,10,101)
pl.plot(x,y,"ro")
 
for kind in ["nearest","zero","slinear","quadratic","cubic"]:#插值方式
    #"nearest","zero"为阶梯插值
    #slinear 线性插值
    #"quadratic","cubic" 为2阶、3阶B样条曲线插值
    f=interpolate.interp1d(x,y,kind=kind)
    # ‘slinear’, ‘quadratic’ and ‘cubic’ refer to a spline interpolation of first, second or third order)
    ynew=f(xnew)
    pl.plot(xnew,ynew,label=str(kind))
pl.legend(loc="lower right")
pl.show()
————————————————
版权声明：本文为CSDN博主「空城0707」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/huozi07/article/details/50538749