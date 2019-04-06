import os

os.getcwd()
os.chdir('d:\\大三下\\Python与深度学习')

import requests
import re
import urllib
import numpy as np
import utils as u
import tkinter as tk
import time
import tkinter.messagebox as tm
#调整工作路径


#调查主体：Amazon lipstick分类中所有品牌，以及所有品牌下的所有商品
#已实现功能：
#1.获取热品牌分类和按字母索引分类中的所有品牌名称和品牌链接
#2.获取指定品牌下的所有商品名称，下载图片，获取价格和评分
#3.结合1.2中获得的数据，考察品牌与价格，品牌与评分关系
#4.筛选出低价品牌，高价品牌，口碑品牌（平均评分高且评价率高）和性价比品牌（综合价格口碑）
#功能展示过程设计如下：由于调查所有品牌（300+）数据量很大，故在此将品牌范围限制在热门品牌中（共51个）展示以上功能

#索引衔接字符串
for_ind='&indexField='
#lipstick品牌网址基本形式
url='https://www.amazon.com/s/other?k=lipstick&rh=n%3A3760911%2Cn%3A11058281%2Cn%3A11059031%2Cn%3A11059111&pickerToList=lbr_brands_browse-bin'
#Amazon官网
ur='https://www.amazon.com'

#1.获取热品牌分类中的所有品牌名称和品牌链接
Hot=u.Tag(url,0)
u.Tag(url,0)
#热门品牌名称
Hot.print_brandlist()

#2.获取指定品牌下的所有商品名称，下载图片，获取价格和评分，以brandlist中第一个品牌aliveGOT为例
b=u.Brand(Hot.list[47])
#产品名称
b.print_goodlist()
#下载图片
#b.download()
#获取价格
time.sleep(40)
p=b.price()
#评分
time.sleep(40)
s=b.star()

#mean_price=[2.965,4.86]
#mean_star=[2.58,3.83]
#rate=[0.104,0.208]

#rate=[0.10416666666666667,0.20833333333333334,0.75,0.625,0.6666666666666666,0.9791666666666666,0.625,0.9591836734693877,0.3541666666666667,0.1875]
#mean_price=[2.965,4.860833333333333,8.670243902439024,39.14290322580646,16.76151515151515,31.714166666666667,21.588837209302323,11.577777777777778,3.117083333333334,3.2743750000000005,48.357142857142854,36.27717391304348,55.14868421052633,33.966571428571434,10.866666666666667,3.6347499999999995,12.299166666666666,1.265625,17.200833333333332,7.981707317073172]
#mean_star=[2.58,3.8299999999999996,4.052777777777778,3.9233333333333333,3.878125,4.163829787234041,3.886666666666667,4.046808510638298,2.8058823529411767,3.5888888888888886,4.260869565217392,4.151219512195122,0,3.968965517241379,0,3.042857142857143,2.977777777777777,2.4,3.992592592592592,4.033333333333333]


for i in range(10):
    b=u.Brand(Hot.list[i+10])
    time.sleep(5)
    #p=b.price()
    #p=np.mean(p)
    #mean_price.append(p)
    #time.sleep(5)
    s=b.star()
    r=len(s)/b.num
    #s=np.mean(s)
    #mean_star.append(s)
    rate.append(r)
    time.sleep(5)
    i+1
    print(i)

def begin_download():
	downp=var_downpage.get()
	downn=var_downname.get()
	pic.download(downn,int(downp))
class Window:
	def __init__(self,x0=0,x1=50,y0=10,y1=50,y2=90):
		self.x0=0
		self.x1=50
		self.y0=10
		self.y1=50
		self.y2=90

window=Window()
window.show()

#rate[0.10416666666666667,0.20833333333333334,0.75,0.625,0.6666666666666666,0.9791666666666666,0.625,0.9591836734693877,0.3541666666666667,0.1875]
#mean_price[2.965,4.860833333333333,8.670243902439024,39.14290322580646,16.76151515151515,31.714166666666667,21.588837209302323,11.577777777777778,3.117083333333334,3.2743750000000005,48.357142857142854,36.27717391304348,55.14868421052633,33.966571428571434,10.866666666666667,3.6347499999999995,12.299166666666666,1.265625,17.200833333333332,7.981707317073172]
#mean_star=[2.58,3.8299999999999996,4.052777777777778,3.9233333333333333,3.878125,4.163829787234041,3.886666666666667,4.046808510638298,2.8058823529411767,3.5888888888888886,4.260869565217392,4.151219512195122,nan,3.968965517241379,nan,3.042857142857143,2.977777777777777,2.4,3.992592592592592,4.033333333333333]

def Blist():
    #index=index.get()
    #B=u.Tag(url+for_ind+index,0)
    B=Hot
    blist=''
    for brand in B.list:
        blist=blist+brand[0]+'\n'
    tm.showinfo(title='Brand List', message=blist)
        
    
class Window1:
	
    def __init__(self,x0=0,x1=50,y0=10,y1=50,y2=90):
        self.x0=0
        self.x1=50
        self.y0=10
        self.y1=50
        self.y2=90

    def show(self):
        root = tk.Tk()
        #canvas = tk.Canvas(root, height=200, width=500)
        #image_file = tk.PhotoImage(file='d:\\大三下\\Python与深度学习\\Amazon.gif')
        #image = canvas.create_image(0,0, anchor='nw', image=image_file)
        #canvas.pack(side='top')
        tk.Label(root, text='Index: ').place(x=self.x0, y= self.y0)
        var_index = tk.StringVar()
        entry_downname = tk.Entry(root, textvariable=var_index).place(x=self.x1, y= self.y0)
        tk.Button(root,command=Blist,width=15,height=2,text='search').place(x=self.x1, y= self.y2)
        root.mainloop()


window=Window1()
window.show()

def Glist():
    #brand=var_O1.get()
    #b=u.Brand(Hot.list[3])
    glist=''
    for item in b.list:
        glist=glist+item[0]+'\n'
    tm.showinfo(title='Goods List', message=glist)

def down():
   #brand=var_O1.get()
   #b=u.Brand(Hot.list[3])
    b.download()
    
class Window2:
    def __init__(self,x0=0,x1=50,y0=10,y1=50,y2=90):
        self.x0=0;self.x1=50;self.y0=10;self.y1=50;self.y2=100;self.y3=110
    def show(self):
        root = tk.Tk()
       
        tk.Label(root, text='Brand:').place(x=self.x0, y= self.y0)
        var_O1 = tk.StringVar();var_O2 = tk.StringVar()
        entry_downname = tk.Entry(root, textvariable=var_O1).place(x=self.x1, y= self.y0)
        tk.Button(root,command=Glist,width=15,height=2,text='search').place(x=self.x1, y= self.y1)
        tk.Button(root,command=down,width=15,height=2,text='download').place(x=self.x1, y= self.y3)
        root.mainloop()
        

window=Window2()
window.show()

rate
mean_price
mean_star
def Top(mode):
    bl=''
    if mode==1:
        o=np.argsort(mean_price)[0:5]
        for i in o:
            bl=bl+Hot.list[i][0]+'\n'
    if mode==2:
        o=np.argsort(mean_price)[-7:-1]
        for i in o:
            bl=bl+Hot.list[i][0]+'\n'
    if mode==3:
        o1=np.argsort(mean_star)
        o2=np.argsort(rate)
        o=np.argsort(o1+o2)[-6:-1]
        for i in o:
            bl=bl+Hot.list[i][0]+'\n'
    if mode==4:
        o1=np.argsort(mean_star)
        for j in range(50):
            mean_price[j]=mean_price[j]*-1
            
        o2=np.argsort(mean_price)
        o=np.argsort(o1+o2)[-6:-1]
        for i in o:
            bl=bl+Hot.list[i][0]+'\n'
    print(bl)

Top(1)
Top(4)
