#utf-8
import requests
from lxml import etree
import re
import os
import os.path
import json

def getHtml():
    #headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'} 
    r = requests.get(
        '''http://www.win4000.com/meitu.html''')
    #r.text
    #r.raise_for_status()
    #r.encoding = r.apparent_encoding
    #b = json.loads(r.text)
    print(r.text)
    return r.text

def getimage():
    html = getHtml()
    #print(html)
    h = etree.HTML(html,etree.HTMLParser())
    fileHandle = open ( 'test.txt', 'w' )
    t = 21
    print(h.xpath('//ul[@class="clearfix"]'))
    for item in h.xpath('//ul[@class="clearfix"]/li/a/img/@data-original'):
        print(item)
        imgYrl = "./image/%s.jpg"%(t)
        imgU = "./image"
        if not os.path.exists(imgU):
            os.makedirs(imgU)
        else:
            fileHandle.write(item+"\n")
            r = requests.get(item)
            with open(imgYrl, 'wb') as f:
                f.write(r.content)
        t += 1
    fileHandle.close()
    print("ok")

if  __name__ == "__main__":
    getimage()
