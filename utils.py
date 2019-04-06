import requests
import re
import os
import urllib

#模拟登陆
#分析网址
#爬虫主体：Amazon lipstick分类中所有品牌的所有商品
for_ind='&indexField='#索引衔接字符串
url='https://www.amazon.com/s/other?k=lipstick&rh=n%3A3760911%2Cn%3A11058281%2Cn%3A11059031%2Cn%3A11059111&pickerToList=lbr_brands_browse-bin'#lipstick品牌网址基本形式
ur='https://www.amazon.com'#Amazon官网

##问题：实际拿到的HTML和网页上顺序有区别
#解码，写入文件，找规律
##正则表达式\n后面接字母出错

#爬取Amazon lipstick 热门品牌


#类1：Tag
#用于储存指定字母索引下的所有品牌的名称和品牌网址
#类变量 name：Hot Brand or Brand by index_x, list：列表，num：品牌数量
#init：初始化，建立品牌的名称和品牌链接的列表
#print_brandlist：打印品牌名称和网址
class Tag(object):
    
    def __init__(self,url,index):#index==0,热门品牌  #index==字母，字母索引下所有品牌
        if index==0:
            ht=requests.get(url,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'})
            self.name='Hot Brand'
        else:
            ht=requests.get(url+for_ind+index,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'})
            self.name='Brand by index_'+index
        html=ht.text
        ilist=re.findall('title\=\".*?\" href\=\".*?\"', html)#规律
        n=len(ilist)
        brandlist=[]
        for item in ilist:
            #品牌名brandname 
            bname=re.search('title\=\".*?\"',item).group()
            bname=eval(bname[6:])
            #品牌链接 brandurl
            burl=re.search('href\=\".*?\"',item).group()
            burl=eval(burl[5:])
            burl=ur+burl
            brandlist.append([bname,burl])
        self.list=brandlist
        self.num=n
    
    def print_brandlist(self):
        for i in range(self.num):
            print(self.list[i][0])
    
#类2：Brand
#用于储存指定品牌下的所有商品的名称和商品链接
#类变量 name：品牌名, list：列表，num：商品数量
#init：初始化，建立商品的名称和商品链接的列表
#print_goodlist：打印商品名称和网址 
#download：下载商品图片到以品牌名命名的文件夹，图片以商品名命名
#price：获取所有商品价格
#star：获取商品的评分（五分制，一些商品肯没有评分）
class Brand(object):
    def __init__(self,brand):#brand[0]品牌名 brand[1]品牌链接
        self.name=brand[0]
        self.url=brand[1]
        ht=requests.get(brand[1],headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'})
        html=ht.text
        ilist=re.findall('href\=\".*?\">\n.*\n.*img src\=\".*?\"\n.*\n.*alt\=\".*?\"',html) 
        ilist=ilist[1:]#去掉第一个广告
        n=len(ilist)
        goodlist=[]
        for item in ilist:
            h=re.search('href\=\".*\"',item).group()
            h=eval(h[5:])
            name=h[1:h.find('/dp')]
            pu=re.search('img src\=\".*.\"',item).group()
            pu=eval(pu[8:])
            iur=ur+h
            goodlist.append([name,pu,iur])
        self.list=goodlist
        self.num=n
        #goodlist[0] 产品名 goodlist[1] 图片链接 goodlist[2] 产品链接
    
    def print_goodlist(self):
        for i in range(self.num):
            print(self.list[i][0])       
    
    def download(self):
        os.makedirs('\\大三下\\Python与深度学习\\'+self.name)
        local='\\大三下\\Python与深度学习\\'+self.name+'\\'
        for item in self.list:
            loc=local+item[0]+'.jpg'
            urllib.request.urlretrieve(item[1],loc)
            
    def price(self):
        price=[]
        ht=requests.get(self.url,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'})
        html=ht.text
        ilist=re.findall('<span class\="a-offscreen">.*?<',html)
        for p in ilist:
            p=p[27:-1]
            if len(p)>6:
                break
            else:
                price.append(float(p)) 
        return price
    def star(self):
        star=[]
        ht=requests.get(self.url,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'})
        html=ht.text
        ilist=re.findall('\"a-icon-alt\">.*? ',html)
        for s in ilist:
            star.append(float(s[13:-1]))
        return star

         
    





#爬取每个品牌的所有商品名称价格，评分，销量
#整合多行爬取减少错误
#价格不好爬
#plist<-re.findall('<span class="a-price".*')
#去除第一个
#   local='d:\\goods\\Princessa Aloe Lipsticks Set - 12 Fashionable Colors/ Long Lasting.jpg' 文件名

#产品列表 名字 图片 网址
