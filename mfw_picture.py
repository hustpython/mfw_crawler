'''@author: yzw
'''
#!/usr/bin/python  
# -*- coding:utf-8 -*-  
import urllib
from urllib import request
from bs4 import BeautifulSoup
import re
import os
import time
mfw_url= str(input('请输入你喜欢的游记的网址：\n'))
req=urllib.request.Request(mfw_url)
res=urllib.request.urlopen(req).read().decode('utf-8')
soup = BeautifulSoup(res, 'html.parser')
title = soup.find_all('title')
title=str(title)
title1=title.rfind("图片")
title=title[:title1]
title2=title.rfind(",")
title=title[:title2]
title=title.replace("[<title>", '')
print("游记标题："+'\n'+"        "+str(title))
a = soup.select('._j_lazyload')
leng=len(a)
print("游记中共有 %d 张图片" %leng)
i= 1
imgPath=r'H:\%s'%str(title)
if not os.path.isdir(imgPath):
    os.mkdir(imgPath)
t1 = time.time()
list=[]

txtname=str(imgPath+"\图片信息.txt")
if os.path.exists(txtname):
    print ('图片信息已经存在')
else:
    f =open(txtname, 'w')
    f.write("游记网址："+mfw_url+'\n'+"游记标题："+title)
    f.close()
    print('图片信息已生成')

for content in a:
    content =str(content)
    pos = content.rfind("?")
    e=content[:pos]
    d=e.rfind(":")
    s=e[d:]
    s="http"+s
    list.append(s)
for i in range(leng) :
    ext=list[i].rfind(".")
    ext=list[i][ext:]
    j=i+1
    imgname=r'H:\%s\%s' %(str(title),str(j)+ext)
    if os.path.exists(imgname):
       print ('第 %d张图片已经存在，无需下载'%j)
    else:
        s1=urllib.request.urlopen(list[i]).read()
        filename=os.path.join(imgPath,str(j)+ext)
        with open(filename,'wb') as f:
             f.write(s1)
             print('第 %d张图片下载成功'%j)

t2=time.time()
t=t2-t1
f=int(t/60)
m=t%60
print('所有图片下载完毕,一共用时%d分钟,%.1f秒' %(f,m))