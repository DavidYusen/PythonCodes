# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import logging
import time
import re
import csv

pudonglist = ["beicai", "biyun", "caolu", "chuansha", "datuanzhen", "gaodong",
                "gaohang", "geqing", "hangtou", "huamu", "huinan",
                "jinqiao", "jinyang", "kangqiao", "laogangzhen",
                "lianyang", "lingangxincheng", "lujiazui", "nanmatou",
                "nichengzhen", "sanlin", "shibo", "shuyuanzhen",
                "tangqiao", "tangzhen", "waigaoqiao", "wanxiangzhen",
                "weifang", "xinchang", "xuanqiao", "yangdong",
                "yangjing", "yuanshen", "yuqiao1", "zhangjiang", "zhoupu", "zhuqiao"]


def initlogging(logfilename):
    logging.basicConfig(filename=logfilename,
                        filemode="w",
                        format="%(asctime)s %(name)s:%(levelname)s:%(message)s",
                        datefmt="%d-%M-%Y %H:%M:%S",
                        level=logging.INFO)
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('LINE %(lineno)-4d : %(levelname)-8s %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)


def getresponsefromurl(url):
    for i in range(3):
        try:
            user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
            headers = {'User-Agent': user_agent}
            req = requests.get(url, headers=headers, timeout=20)
            break
        except requests.exceptions.ConnectionError:
            logging.error('ConnectionError -- please wait 3 seconds')
            time.sleep(3)
        except requests.exceptions.ChunkedEncodingError:
            logging.error('ChunkedEncodingError -- please wait 3 seconds')
            time.sleep(3)
        except:
            logging.error('UUnknow Error Happened, Please wait 3 seconds')
            time.sleep(3)
    return req


def findStr(startStr, orgStr, endStr):
    startLoc = orgStr.find(startStr)
    if startLoc != -1:
        startLoc = orgStr.find(startStr) + len(startStr)
    else:
        return ''
    endLoc = orgStr.find(endStr, startLoc)
    if startLoc != -1 and endLoc != -1:
        rtnStr = orgStr[startLoc:endLoc].strip()
    else:
        rtnStr = ''
    return rtnStr


def handlelinks(pageUrl):

    html = getresponsefromurl(pageUrl)
    bsObj = BeautifulSoup(html.content, 'lxml')

    price = bsObj.find("div", {"class": "price"})
    price = findStr(u'<span class=\"total\">', str(price), u'</span')

    unitPrice = bsObj.find("div", {"class": "unitPrice"})
    unitPrice = findStr(u'<span class=\"unitPriceValue\">', str(unitPrice), u'<i>')

    # aroundInfo = bsObj.find("div", {"class": "aroundInfo"})
    # logging.info(aroundInfo)

    communityName = bsObj.find("div", {"class": "communityName"})
    g = communityName.stripped_strings
    logging.info(next(g))
    communityName = next(g)

    areaName = bsObj.find("div", {"class": "areaName"})
    g = areaName.stripped_strings
    logging.info(next(g))
    area = next(g)
    position = next(g)
    try:
        circlearea = next(g)
    except StopIteration:
        circlearea = ''

    introContent = bsObj.find("div", {"class": "introContent"})
    room = findStr(u'房屋户型</span>', str(introContent), u'</li>')
    floor = findStr(u'所在楼层</span>', str(introContent), u'</li>')
    areas = findStr(u'建筑面积</span>', str(introContent), u'</li>')
    huxing = findStr(u'户型结构</span>', str(introContent), u'</li>')
    orientation = findStr(u'房屋朝向</span>', str(introContent), u'</li>')
    structure = findStr(u'建筑结构</span>', str(introContent), u'</li>')
    decorate = findStr(u'装修情况</span>', str(introContent), u'</li>')
    elavatorRate = findStr(u'梯户比例</span>', str(introContent), u'</li>')
    elavator = findStr(u'配备电梯</span>', str(introContent), u'</li>')
    duration = findStr(u'产权年限</span>', str(introContent), u'</li>')
    bighousetype = findStr(u'别墅类型</span>', str(introContent), u'</li>')

    # aroundInfo = bsObj.find("div", {"class": "transaction"})
    # logging.info(aroundInfo)
    # starttosell = findStr(u'挂牌时间</span><span>', str(introContent), u'</li>')
    # housetype = findStr(u'交易权属</span><span>', str(introContent), u'</li>')
    # lasttrade = findStr(u'上次交易</span><span>', str(introContent), u'</li>')
    # indexNo = findStr(u'房源编号：', str(aroundInfo), u'</span>')

    return [area, position, communityName, circlearea,price, unitPrice, room, areas, floor, huxing, orientation, elavatorRate, decorate, duration,
                structure, elavator, bighousetype, pageUrl]


if __name__ == '__main__':

    initlogging("main.log")
    logging.info('start main process')
    url = "https://sh.lianjia.com/ershoufang/107100638916.html"
    estateContent = handlelinks(url)
    logging.info(estateContent)


