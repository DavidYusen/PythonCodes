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
            tsObj = BeautifulSoup(html)
        except Exception as e:
            print("Try BeautifulSoup again failed")
    return tsObj


# ------------------------------------------------------------------------------
def handleLinks(pageUrl):
    global CountNo

    try:
        print("Processing " + "http://sh.lianjia.com" + pageUrl)
        html = urlopen("http://sh.lianjia.com" + pageUrl)
    except urllib.URLError as e:
        print("Url Error!!!!\n")
        time.sleep(60)
        return ['']
    else:
        bsObj = BeautifulSoup(html)

        houseInfo = bsObj.find("div", {"class": "houseInfo"})
        price = findStr(u'<div class="mainInfo bold" style="font-size:28px;">', str(houseInfo), u'<span')
        room = findStr(u'class="mainInfo">', str(houseInfo), u'<span')
        ting = findStr(u'span class="unit">', str(houseInfo), u'<span')

        introContent = bsObj.find("div", {"class": "area"})
        size = findStr(u'class="mainInfo">', str(introContent), u'<span')

        introContent = bsObj.find("div", {"class": "aroundInfo"})
        area = findStr(u'addrEllipsis" title="', str(introContent), u'">')

        introContent = bsObj.find("div", {"class": "houseRecord"})
        indexNo = findStr(u'houseNum">房源编号：', str(introContent), u'</span')

        CountNo = CountNo + 1
        return [indexNo, price, room, ting, size, area]


# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
html = urlopen("http://sh.lianjia.com/zufang/")
bsObj = BeautifulSoup(html)

# nameList：总套数
numbers = bsObj.find("div", {"class": "list-head clear"})
totalnum = findStr(u'为您找到<span>', str(numbers), u'</span')
# nameList = bsObj.findAll("strong")
# maxCount：每页20条记录，总页数
maxCount = int(math.ceil(int(totalnum) / 20)) + 1
# fileName：生成的文件名，20170108的格式
fileName = str(time.strftime('%Y%m%d', time.localtime(time.time())))

pages = set()
# math.ceil()返回大于该值的最小浮点型整数
#fileNo = int(math.ceil(i / pageBreakNo))
# FILE_BOJECT = open("%s_%.0f.csv" % (fileName, fileNo), "ab")
FILE_BOJECT = open("%s_rent.csv" % (fileName), "w")
writer = csv.writer(FILE_BOJECT)
# ------------------------------------------------------------------------------
for i in range(1, (int(totalnum))):
    html = None
    # print ("File: %s_%.0f.csv, TotalPage: %d, PageNo: %d" % (fileName, fileNo, maxCount, i))
    try:
        # html：每页20套房源的第几页
        html = urlopen("http://sh.lianjia.com/zufang/d" + str(i), timeout=5)
    except urllib.URLError as e:
        print("Url Error!!!!\n")
        time.sleep(60)
    else:
        print("Processing " + "http://sh.lianjia.com/zufang/d" + str(i))
        bsObj = BeautifulSoup(html)

        nameList = bsObj.findAll("strong")
        maxCount = int(math.ceil(int(totalnum) / 20)) + 1

        linkList = bsObj.findAll(href=re.compile("\/zufang\/shzr[0-9]+\.html"))
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
