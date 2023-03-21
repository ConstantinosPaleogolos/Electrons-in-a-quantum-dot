#--------------------------------------------
#导入模块：导入txt数据为数组
import os
import numpy as np
import matplotlib.pyplot as plt

#--------------------------------------------
#读取模块，把每行读取为一个数组，每个字符是一个元素
file=open('C:/Users/Pc/Desktop/muonflux_Pb.txt','r')
arr = file.readlines()
longueur=len(arr)
print(longueur)

#--------------------------------------------
#清洗模块，把数据全部变成正规形式
i=0
nouveaux_donnees=[]
#nouveaux_donnees为清洗后的数据，法语新数据

while 0<=i<longueur:
    donnee=[]
    transfert=''
    #选定第i行，i为行指标
    #donnee为储存一行的新数组，法语数据，transfert为中转字符串，法语中转
    j=1
    while 1<=j<len(arr[i]):
        #选定第i行第j个元素，从第二个开始
        
        if arr[i][j]!=' ' and j!=len(arr[i])-1:
            transfert+=arr[i][j]
            #把每个元素怼入中转字符串
        
        elif arr[i][j]!=' ' and j==len(arr[i])-1:
            transfert+=arr[i][j]
            Gleikommazahl=float(transfert)
            donnee.append(Gleikommazahl)
            transfert=''
            #每次遇到空格，则把中转字符串转化，加入，再置零
            #Gleikommazahl是德语浮点数
            #这是处理最后一位不是空格的情况
            
        else:
            Gleikommazahl=float(transfert)
            donnee.append(Gleikommazahl)
            transfert=''
            #每次遇到空格，则把中转字符串转化，加入，再置零
            #Gleikommazahl是德语浮点数
            #这是处理后面是空格的情况
            
        j+=1
    i+=1
    nouveaux_donnees.append(donnee)
    #把生成的donnee存入nouveaux_donnee
    
#--------------------------------------------
#计算模块
Theta=[]
Phi=[]

px=[]
py=[]
pz=[]

#数据存储模块
i=0
while 0<=i<len(nouveaux_donnees):
    px.append(nouveaux_donnees[i][0])
    py.append(nouveaux_donnees[i][1])
    pz.append(nouveaux_donnees[i][2])
    i+=1

i=0

#数据计算模块
while 0<=i<len(px):
    if px[i]>=0 and py[i]>=0 and pz[i]>=0:
        phi=np.arccos(px[i]/np.sqrt(px[i]**2+py[i]**2))
        theta=np.arccos(-pz[i]/np.sqrt(px[i]**2+py[i]**2+pz[i]**2))
    
    if px[i]>=0 and py[i]>=0 and pz[i]<0:
        phi=np.arccos(px[i]/np.sqrt(px[i]**2+py[i]**2))
        theta=np.arccos(-pz[i]/np.sqrt(px[i]**2+py[i]**2+pz[i]**2))
    
    if px[i]>=0 and py[i]<0 and pz[i]>=0:
        phi=2*np.pi-np.arccos(px[i]/np.sqrt(px[i]**2+py[i]**2))
        theta=np.arccos(-pz[i]/np.sqrt(px[i]**2+py[i]**2+pz[i]**2))
    
    if px[i]>=0 and py[i]<0 and pz[i]<0:
        phi=2*np.pi-np.arccos(px[i]/np.sqrt(px[i]**2+py[i]**2))
        theta=np.arccos(-pz[i]/np.sqrt(px[i]**2+py[i]**2+pz[i]**2))
    
    if px[i]<0 and py[i]>=0 and pz[i]>=0:
        phi=np.arccos(px[i]/np.sqrt(px[i]**2+py[i]**2))
        theta=np.arccos(-pz[i]/np.sqrt(px[i]**2+py[i]**2+pz[i]**2))
    
    if px[i]<0 and py[i]>=0 and pz[i]<0:
        phi=np.arccos(px[i]/np.sqrt(px[i]**2+py[i]**2))
        theta=np.arccos(-pz[i]/np.sqrt(px[i]**2+py[i]**2+pz[i]**2))
    
    if px[i]<0 and py[i]<0 and pz[i]>=0:
        phi=2*np.pi-np.arccos(px[i]/np.sqrt(px[i]**2+py[i]**2))
        theta=np.arccos(-pz[i]/np.sqrt(px[i]**2+py[i]**2+pz[i]**2))
    
    if px[i]<0 and py[i]<0 and pz[i]<0:
        phi=2*np.pi-np.arccos(px[i]/np.sqrt(px[i]**2+py[i]**2))
        theta=np.arccos(-pz[i]/np.sqrt(px[i]**2+py[i]**2+pz[i]**2))
    
    Theta.append(theta*180/np.pi)
    Phi.append(phi*180/np.pi)
    i+=1

#--------------------------------------------
#撸图模块
def peindre_phi():
    plt.close()
    plt.hist(Phi,bins=360,edgecolor='g',histtype='step')
    plt.title("Angle between x and y:phi")
    plt.xlabel("Phi")
    plt.xlim(0,360)
    plt.ylabel("Numéro de Fréquence")
    plt.show()

def peindre_theta():
    plt.close()
    plt.hist(Theta,bins=180,edgecolor='r',histtype='step')
    plt.title("Angle with z:theta")
    plt.xlabel("Phi")
    plt.ylabel("Numéro de Fréquence")
    plt.xlim(0,180)
    plt.show()

peindre_theta()
peindre_phi()








