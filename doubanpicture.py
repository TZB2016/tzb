# -*- coding:utf-8 -*-
# 2013.12.36 19:41 wnlo-c209
# 抓取dbmei.com的图片。
import socket
import http.cookiejar
from bs4 import BeautifulSoup
import os, sys, urllib
from urllib import parse,request
from urllib.request import urlopen
# 创建文件夹，昨天刚学会
from random import choice

my_headers=[#"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",  
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",  
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0"  
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",  
"Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)"  
"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0"    
]  
def get_content(url,headers,page):  
  
    randdom_header=choice(headers)  
  
    req=urllib.request.Request(url)  
    req.add_header("User-Agent",randdom_header)  
    req.add_header("Host","img3.doubanio.com")  
    req.add_header("Referer","https://www.douban.com/photos/photo/page/large")  
    req.add_header("GET",url)  
  
    content=urlopen(req)
    print(content)  
    return content  
  

path = os.getcwd()   				     # 获取此脚本所在目录
new_path = os.path.join(path,u'doubai')
if not os.path.isdir(new_path):
	  os.mkdir(new_path)
print(new_path)
def page_loop(page=2180968373):
       try:         
           url = 'https://www.douban.com/photos/photo/%s/large' % page
          # print(url)
          #urlcontent=get_content(url,my_headers,page)
           #print(urlcontent) 
           #urlcontent=urlopen(url)          
          # print(urlcontent.getcode())
           if 0:
                   print ('eeeeeeeeeeeeeeeeeeeeeeee')
           else:
               #content=urlcontent.read()
               content=get_content(url,my_headers,page).read()
               #print(content)
               soup = BeautifulSoup(content,'html.parser')
               my_girl = soup.find('td',id='pic-viewer').find_all('img')
               #my_girl = soup.find_all('img')
               if my_girl ==[]:
                      print (u'111111111111111111')
               else:
       	              print (u'2222222222')
               
               for girl in my_girl:
                             link = girl.get('src')
		             #flink = 'http://www.dbmeizi.com/' + link
                             print (link)
                             content2 =urlopen(link).read()
                             with open(u'doubai'+'/'+link[-15:],mode="wb") as code:#在OSC上现学的
                                     code.write(content2)
                                     #code.close()
       except urllib.error.HTTPError as reason:#when discover the httperror ,except the error .For example 404 ,not have web page
                print(reason)                    
       page = int (page) + 1
       print (u'333333333333')
       print ('the %s page' % page)
       page_loop(page)	
page_loop()
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~END~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#为了避免双击的时候直接一闪退出，在最后面加了这么一句
raw_input("Press <Enter> To Quit!")