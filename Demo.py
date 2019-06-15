import requests
from lxml import etree
import re
import os
import os.path
import json


def getHtml(html):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'} 
    r = requests.get(
        '''http://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E7%BE%8E%E5%A5%B3&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&hd=&latest=&copyright=&word=%E7%BE%8E%E5%A5%B3&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=1&fr=&expermode=&force=&cg=girl&pn=30&rn=30&gsm=1e&1560073329836=''',headers = headers,timeout=30)
    #r.text
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    b = json.loads(r.text)
    #print(b)
    return b

def getimage():
    html = getHtml("")
    #print(html)
    h = etree.HTML(html,etree.HTMLParser())
    fileHandle = open ( 'test.txt', 'w' )
    t = 200
    #print(h.xpath('//img[@class="main_img img-hover"]/@data-imgurl'))
    for item in h.xpath('//img[@class="main_img img-hover"]/@data-imgurl'):
        imgYrl = "./image/%s.jpg"%(t)
        imgU = "./image"
        if not os.path.exists(imgU):
            os.makedirs(imgU)
        else:
            fileHandle.write(item+"\n")
            r = requests.get(item)
            with open(imgYrl, 'wb') as f:
                f.write(r.content)
        t -= 1
        if(t==0):
            break
            
    
    fileHandle.close()
    print("ok")
       



def getimg():
    b = getHtml("")
    count = 0
    for key in b:
        if key=="data":
            for value in b[key]:
                imgYrl = "./image/%s.jpg"%(count)
                imgU = "./image"
                if not os.path.exists(imgU):
                   os.makedirs(imgU)
                else:
                    if value.get('thumbURL') == None:
                        break
                    else:
                        print(value.get('thumbURL'))
                        r = requests.get(value.get('thumbURL'))
                        print(r.content)
                with open(imgYrl, 'wb') as f:
                    f.write(r.content)
                count += 1
    print('ok')
if  __name__ == "__main__":
    getimg() 
