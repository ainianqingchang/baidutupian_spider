#!/usr/bin/python3

import re
import requests
import os


word=input("please input your search:")
pn=input("number you want to catch:")
pn=int(int(pn)/60)
print("pn=",pn)
j=0
stodir=os.environ['HOME']+'/Desktop/'+word
if not os.path.exists(stodir):
    os.mkdir(stodir)
while j<pn:
    url='https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word='+word+'&pn='+str(j*60)+'&gsm=3c&ct=&ic=0&lm=-1&width=0&height=0'
    response=requests.get(url)
    string=response.text    
    pic_url=re.findall(r'"objURL":"(.*?)",',string,re.S)
    i=0
    for each in pic_url:
        print(each)
        if re.match(r'(.*?).png',each):
            print('OKOKOKOK')
            try:
                pic=requests.get(each,timeout=2)
            except requests.exceptions.ConnectionError:
                print('[错误]当前图片无法下载')
                continue
            except e:
                print('Other exception...')
                continue
    
            str_deal='picture_'+str(j)+'_'+str(i)+'.png'
            print(str_deal)
            fp=open(stodir+'/'+str_deal,'wb')
            
            fp.write(pic.content)
            fp.close()
            i+=1
        else:
            try:
                pic=requests.get(each,timeout=2)
            except requests.exceptions.ConnectionError:
                print('[错误]当前图片无法下载')
                continue
            except:
                print('Other exception...')
                continue

            str_deal='picture_'+str(j)+'_'+str(i)+'.jpg'
            fp=open(stodir+'/'+str_deal,'wb')
            fp.write(pic.content)
            fp.close()
            i+=1
    j+=1