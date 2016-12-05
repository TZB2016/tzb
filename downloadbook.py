import re,urllib
from urllib import parse,request
from urllib.request import urlopen
from bs4 import BeautifulSoup


root = 'http://novel.hongxiu.com'
root1 = 'http://novel.hongxiu.com/a/901957/list.html'
urlList = [];
print (u"ereter1111111111111...")
soup = BeautifulSoup(urlopen('http://novel.hongxiu.com/a/901957/list.html').read(), 'html.parser')
#novelname = soup.find('div',id='htmlList').find('a').get_text()
for result in soup.find('div',id="htmlList").find_all('li'):
        res = result.find_next("a")
        print(u'zhangjie==='+res.get_text())
        urlList.append(res['href'])
fileHandle = open('tzb'+u'.txt',mode="w",encoding='utf-8')
for result in urlList:
        print('222222222'+result)
        temp =BeautifulSoup(urlopen(root+result).read(),'html.parser')
        print (u"333333333333:"+temp.title.text)
        content = temp.find(id="htmlContent").get_text()
        fileHandle.write(content)
fileHandle.close()
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~END~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")