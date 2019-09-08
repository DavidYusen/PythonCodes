# -*- coding: utf-8 -*-

import urllib
from urllib.request import urlopen
from urllib.request import urlparse
from bs4 import BeautifulSoup
import re
import datetime
import time
import random
import csv
import io
import math
import socket
import logging

# 存储抓取网页的个数
CountNo = 0       

# 每多少页存储在一个文件里
pageBreakNo = 200       

# 超时30s
socket.setdefaulttimeout(30)

logging.basicConfig()

# 查找在orgStr中，startStr与endStr之间的字符串


def findstr(startStr, orgStr, endStr):
    startLoc = orgStr.find(startStr) + len(startStr)
    endLoc = orgStr.find(endStr, startLoc)
    if startLoc != -1 and endLoc != -1:
        rtnStr = orgStr[startLoc:endLoc].strip()
    else:
        rtnStr = ''
    return rtnStr


def EnhancedBeautifulSoup(html):
    try:
        tsObj = BeautifulSoup(html, 'lxml')
    except Exception as e:
        print("Try BeautifulSoup again")
        try:
            tsObj = BeautifulSoup(html, 'lxml')
        except Exception as e:
            print("Try BeautifulSoup again failed")
    return tsObj


def handleLinks(pageUrl):

    global CountNo
    
    try:
        print("Processing " + "http://sh.lianjia.com/ershoufang"+pageUrl)
        html = urlopen("http://sh.lianjia.com"+pageUrl) 
    except urllib.URLError as e:
        print("Url Error!!!!\n")
        time.sleep(60)
        return ['']
    else:
        bsObj = EnhancedBeautifulSoup(html)
        
        price = bsObj.find("div", {"class": "price"})
        price = findstr(u'<div class=\"mainInfo bold\">', str(price), u'<span')

        introContent = bsObj.find("div", {"class": "introContent"})
        room = findstr(u'房屋户型：</span>', str(introContent), u'</li>')
        area = findstr(u'建筑面积：</span>', str(introContent), u'平</li>')  
        floor = findstr(u'所在楼层：</span>', str(introContent), u'</li>')
        orientation = findstr(u'朝向：</span>', str(introContent), u'</li>') 
        elavatorRate = findstr(u'梯户比例：</span>', str(introContent), u'</li>')   
        decorate = findstr(u'装修情况：</span>', str(introContent), u'</li>')  
        roomType = findstr(u'房屋类型：</span>', str(introContent), u'</li>') 
        if u'商住'.encode('utf-8') != roomType:
            duration = findstr(u'房本年限：</span>', str(introContent), u'</li>') 
        else:
            duration = '---'
            
        aroundInfo = bsObj.find("table", {"class":"aroundInfo "})
        buildDate = findstr(u'>年代：</span>', str(aroundInfo), u'</td>')  
        residence = findstr(u'html">', str(aroundInfo), u'</a>')
        indexNo = findstr(u'房源编号：', str(aroundInfo), u'</span>')
        
        aroundjs_content = bsObj.find("div", {"class":"around js_content"})   
        if None == aroundjs_content:
            longitude=''
            latitude=''
        else:
            longitude = aroundjs_content["longitude"]
            latitude = aroundjs_content["latitude"]

        CountNo = CountNo + 1
        return [indexNo, price, room, area, floor, orientation, elavatorRate, decorate, roomType, duration, buildDate, residence, longitude, latitude]


if __name__ == '__main__':
    logging.warning('start main process')

    html = urlopen("http://sh.lianjia.com/ershoufang/") 
    bsObj = EnhancedBeautifulSoup(html)
    
    # nameList：总套数
    nameList = bsObj.findAll("strong")
    # maxCount：每页20条记录，总页数  
    maxCount = int(math.ceil(int(nameList[1].get_text())/20)) + 1
    # fileName：生成的文件名，20170108的格式
    fileName = str(time.strftime('%Y%m%d', time.localtime(time.time())))
      
    for i in range(1, (maxCount + 1)):
        pages = set()
        # math.ceil()返回大于该值的最小浮点型整数
        fileNo = int(math.ceil(i/pageBreakNo))
        FILE_BOJECT = open("%s_%.0f.csv" % (fileName, fileNo), "a")
        writer = csv.writer(FILE_BOJECT)   
        html = None
    
        try:
            # html：每页20套房源的第几页，不是到每套房源里面去抓取数据的
            html = urlopen("http://sh.lianjia.com/ershoufang/d"+str(i), timeout=5) 
        except urllib.URLError as e:
            print("Url Error!!!!\n")
            time.sleep(60)
        else:
            print("Processing " + "http://sh.lianjia.com/ershoufang/d"+str(i))
            bsObj = EnhancedBeautifulSoup(html)
            
            nameList = bsObj.findAll("strong")   
            maxCount = int(math.ceil(int(nameList[1].get_text())/20)) + 1
              
            linkList = bsObj.findAll(href=re.compile("\/ershoufang\/sh[0-9]+\.html"))
            for link in linkList:
                if 'href' in link.attrs:
                    if link.attrs['href'] not in pages:
                        # 我们遇到了新页面
                        newPage = link.attrs['href']        
                        estateContent = handleLinks(newPage)
                        pages.add(newPage)
                        writer.writerow(estateContent)
            FILE_BOJECT.close() 
            time.sleep(1)