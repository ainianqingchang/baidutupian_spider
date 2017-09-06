#!/usr/bin/python3

import re
import requests
import os
import imghdr


word=input("please input your search:")
pn=input("number you want to catch:")
pn=int(pn)
print("pn=",pn)
pic_num=0
stodir=os.environ['HOME']+'/Desktop/'+word
if not os.path.exists(stodir):
    os.mkdir(stodir)
while pic_num<pn:
    url='https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word='+word+'&pn='+str(pic_num)+'&gsm=3c&ct=&ic=0&lm=-1&width=0&height=0'
    response=requests.get(url)
    string=response.text    
    pic_url=re.findall(r'"objURL":"(.*?)",',string,re.S)
    i=1
    for each in pic_url:
        print(each)
        if re.match(r'(.*?).(.*?)',each):
            try:
                pic=requests.get(each,timeout=2)
            except requests.exceptions.ConnectionError:
                print('[错误]当前图片无法下载')
                continue
            except:
                print('Other exception...')
                continue
    
            str_deal='picture_'+str(pic_num+i)
            with open(stodir+'/'+str_deal,'wb') as fp:
                fp.write(pic.content)

            os.chdir(stodir)
            typepic=imghdr.what(str_deal)
            
            if isinstance(typepic,str):
                print(str_deal)
                str_deal_1=str_deal+'.'+typepic
                os.rename(str_deal,str_deal_1)
            else:
                os.remove(str_deal)
            if i+pic_num>=pn:
                break
            i+=1
           
    pic_num+=i

