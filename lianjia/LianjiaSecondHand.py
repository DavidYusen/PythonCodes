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

CountNo = 0  # 存储抓取网页的个数
pageBreakNo = 200  # 每多少页存储在一个文件里
socket.setdefaulttimeout(30)

# ------------------------------------------------------------------------------
# Function findStr(startStr, orgStr, endStr)
# 查找在orgStr中，startStr与endStr之间的字符串
# Input：
#   startStr --- 起始字符串
#   orgStr   --- 被搜索的字符串
#   endStr   --- 结束字符串
# Return：
#   rtnStr   --- 返回在orgStr中，startStr与endStr之间的字符串
# ------------------------------------------------------------------------------
def findStr(startStr, orgStr, endStr):
    # startLoc = orgStr.find(startStr.encode('utf-8')) + len(startStr.encode('utf-8'))
    # endLoc = orgStr.find(endStr.encode('utf-8'), startLoc)
    # print (startLoc, endLoc)
    # print("In findStr" + startStr + " : " + endStr)
    startLoc = orgStr.find(startStr) + len(startStr)
    endLoc = orgStr.find(endStr, startLoc)
    if startLoc != -1 and endLoc != -1:
        rtnStr = orgStr[startLoc:endLoc].strip()
    else:
        rtnStr = ''
    return rtnStr

def EnhancedBeautifulSoup(html):
    try:
        tsObj = BeautifulSoup(html)
    except Exception as e:
        print("Try BeautifulSoup again")
        try:
            time.sleep(60)
            tsObj = BeautifulSoup(html)
        except Exception as e:
            print("Try BeautifulSoup again failed")
    return tsObj

# ------------------------------------------------------------------------------
def handleLinks(pageUrl):
    global CountNo

    try:
        print("Processing " + "http://sh.lianjia.com/ershoufang" + pageUrl)
        html = urlopen("http://sh.lianjia.com" + pageUrl)
    except urllib.URLError as e:
        print("Url Error!!!!\n")
        time.sleep(60)
        return ['']
    else:
        bsObj = EnhancedBeautifulSoup(html)

        price = bsObj.find("div", {"class": "price"})
        price = findStr(u'<div class=\"mainInfo bold\">', str(price), u'<span')

        introContent = bsObj.find("div", {"class": "introContent"})
        room = findStr(u'房屋户型：</span>', str(introContent), u'</li>')
        area = findStr(u'建筑面积：</span>', str(introContent), u'平</li>')
        floor = findStr(u'所在楼层：</span>', str(introContent), u'</li>')
        orientation = findStr(u'朝向：</span>', str(introContent), u'</li>')
        elavatorRate = findStr(u'梯户比例：</span>', str(introContent), u'</li>')
        decorate = findStr(u'装修情况：</span>', str(introContent), u'</li>')
        roomType = findStr(u'房屋类型：</span>', str(introContent), u'</li>')
        if u'商住'.encode('utf-8') != roomType:
            duration = findStr(u'房本年限：</span>', str(introContent), u'</li>')
        else:
            duration = '---'

        aroundInfo = bsObj.find("table", {"class": "aroundInfo "})
        buildDate = findStr(u'>年代：</span>', str(aroundInfo), u'</td>')
        residence = findStr(u'html">', str(aroundInfo), u'</a>')
        indexNo = findStr(u'房源编号：', str(aroundInfo), u'</span>')

        aroundjs_content = bsObj.find("div", {"class": "around js_content"})
        if None == aroundjs_content:
            longitude = ''
            latitude = ''
        else:
            longitude = aroundjs_content["longitude"]
            latitude = aroundjs_content["latitude"]

        houseArea = findStr(u'class="areaEllipsis">', str(aroundInfo), u'</span>')


        CountNo = CountNo + 1
        return [indexNo, price, room, area, floor, orientation, elavatorRate, decorate, roomType, duration, buildDate,
                residence, longitude, latitude, houseArea]
# ------------------------------------------------------------------------------

# Main------------------------------------------------------------------------------
html = urlopen("http://sh.lianjia.com/ershoufang/")
bsObj = EnhancedBeautifulSoup(html)

# nameList：总套数
nameList = bsObj.findAll("strong")
# maxCount：每页20条记录，总页数
maxCount = int(math.ceil(int(nameList[1].get_text()) / 20)) + 1
# fileName：生成的文件名，20170108的格式
fileName = str(time.strftime('%Y%m%d', time.localtime(time.time())))

# ------------------------------------------------------------------------------
for i in range(1, (int(nameList[1].get_text()))):
    pages = set()
    #math.ceil()返回大于该值的最小浮点型整数
    fileNo = int(math.ceil(i/pageBreakNo))
    #FILE_BOJECT = open("%s_%.0f.csv" % (fileName, fileNo), "ab")
    FILE_BOJECT = open("%s_%.0f.csv" % (fileName, fileNo), "a")
    writer=csv.writer(FILE_BOJECT)

    html = None
    # print ("File: %s_%.0f.csv, TotalPage: %d, PageNo: %d" % (fileName, fileNo, maxCount, i))
    try:
        # html：每页20套房源的第几页
        html = urlopen("http://sh.lianjia.com/ershoufang/d" + str(i), timeout=5)
    except urllib.URLError as e:
        print("Url Error!!!!\n")
        time.sleep(60)
    else:
        print("Processing " + "http://sh.lianjia.com/ershoufang/d" + str(i))
        bsObj = EnhancedBeautifulSoup(html)

        nameList = bsObj.findAll("strong")
        maxCount = int(math.ceil(int(nameList[1].get_text()) / 20)) + 1

        linkList = bsObj.findAll(href=re.compile("\/ershoufang\/sh[0-9]+\.html"))
        for link in linkList:
            if 'href' in link.attrs:
                if link.attrs['href'] not in pages:
                    # 我们遇到了新页面
                    newPage = link.attrs['href']
                    estateContent = handleLinks(newPage)
                    pages.add(newPage)
                    writer.writerow(estateContent)
        time.sleep(1)
    FILE_BOJECT.close()
# ------------------------------------------------------------------------------
