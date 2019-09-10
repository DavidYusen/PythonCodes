# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from datetime import datetime
import logging
import time
import re
import csv
import CommonFunctions as cf

# pudonglist = ["beicai", "biyun", "caolu", "chuansha", "datuanzhen", "gaodong",
#                 "gaohang", "geqing", "hangtou", "huamu", "huinan",
#                 "jinqiao", "jinyang", "kangqiao", "laogangzhen",
#                 "lianyang", "lingangxincheng", "lujiazui", "nanmatou",
#                 "nichengzhen", "sanlin", "shibo", "shuyuanzhen",
#                 "tangqiao", "tangzhen", "waigaoqiao", "wanxiangzhen",
#                 "weifang", "xinchang", "xuanqiao", "yangdong",
#                 "yangjing", "yuanshen", "yuqiao1", "zhangjiang", "zhoupu", "zhuqiao"]
pudonglist = ["biyun", "caolu"]


def handlelinks(pageUrl):

    html = cf.getresponsefromurl(pageUrl)
    bsObj = BeautifulSoup(html.content, 'lxml')

    price = bsObj.find("div", {"class": "price"})
    price = cf.findStr(u'<span class=\"total\">', str(price), u'</span')

    unitPrice = bsObj.find("div", {"class": "unitPrice"})
    unitPrice = cf.findStr(u'<span class=\"unitPriceValue\">', str(unitPrice), u'<i>')

    # aroundInfo = bsObj.find("div", {"class": "aroundInfo"})
    # logging.info(aroundInfo)

    try:
        g = bsObj.find("div", {"class": "communityName"}).stripped_strings
        communityName = ''
        logging.info(next(g))
        communityName = next(g)
    except Exception as e:
        logging.info('Exception in get communityName:', e.value)

    try:
        g = bsObj.find("div", {"class": "areaName"}).stripped_strings
        area = ''
        position = ''
        circlearea = ''
        logging.info(next(g))
        area = next(g)
        position = next(g)
        circlearea = next(g)
    except Exception as e:
        logging.info('Exception in get areaName:', e.value)

    introContent = bsObj.find("div", {"class": "introContent"})
    room = cf.findStr(u'房屋户型</span>', str(introContent), u'</li>')
    floor = cf.findStr(u'所在楼层</span>', str(introContent), u'</li>')
    areas = cf.findStr(u'建筑面积</span>', str(introContent), u'</li>')
    huxing = cf.findStr(u'户型结构</span>', str(introContent), u'</li>')
    orientation = cf.findStr(u'房屋朝向</span>', str(introContent), u'</li>')
    structure = cf.findStr(u'建筑结构</span>', str(introContent), u'</li>')
    decorate = cf.findStr(u'装修情况</span>', str(introContent), u'</li>')
    elavatorRate = cf.findStr(u'梯户比例</span>', str(introContent), u'</li>')
    elavator = cf.findStr(u'配备电梯</span>', str(introContent), u'</li>')
    duration = cf.findStr(u'产权年限</span>', str(introContent), u'</li>')
    bighousetype = cf.findStr(u'别墅类型</span>', str(introContent), u'</li>')

    # aroundInfo = bsObj.find("div", {"class": "transaction"})
    # logging.info(aroundInfo)
    # starttosell = findStr(u'挂牌时间</span><span>', str(introContent), u'</li>')
    # housetype = findStr(u'交易权属</span><span>', str(introContent), u'</li>')
    # lasttrade = findStr(u'上次交易</span><span>', str(introContent), u'</li>')
    # indexNo = findStr(u'房源编号：', str(aroundInfo), u'</span>')

    return [area, position, communityName, circlearea, price, unitPrice, room, areas, floor, huxing, orientation,
            elavatorRate, decorate, duration, structure, elavator, bighousetype, pageUrl]


if __name__ == '__main__':
    cf.initlogging("Main-%s.log" % datetime.now().strftime('%Y%m%d-%H%M%S'))
    logging.info('start main process')
    url = "http://sh.lianjia.com/ershoufang/"

    for district in pudonglist:
        housepages = set()
        logging.info("start handling district: " + district)
        districturl = url + district + '/'
        req = cf.getresponsefromurl(districturl)
        soup = BeautifulSoup(req.content, 'lxml')
        housecount = int(soup.find_all(class_="total fl")[0].span.string)
        pagecount = housecount // 30 + 1
        logging.info("district " + district + " , " + "house count:" + str(housecount))

        for page in range(1, pagecount+1):
            newurl = districturl + 'pg' + str(page)
            req = cf.getresponsefromurl(newurl)
            soup = BeautifulSoup(req.content, "lxml")
            logging.info('handling directory page ' + str(page))
            linkList = soup.findAll(href=re.compile("ershoufang\/[0-9]+\.html"))
            for link in linkList:
                if 'href' in link.attrs:
                    if link.attrs['href'] not in housepages:
                        newPage = link.attrs['href']
                        housepages.add(newPage)

        FILE_BOJECT = open("%s-%s.csv" % (district, datetime.now().strftime('%Y%m%d-%H%M%S')), "a", newline='')
        writer = csv.writer(FILE_BOJECT)

        # logging.info('handling estate details: ')
        for page in housepages:
            logging.info('start handling: ' + page)
            estateContent = handlelinks(page)
            writer.writerow(estateContent)
            time.sleep(0.1)
            # logging.info(page + ' is done.')

        logging.info(district + " district is done.")


