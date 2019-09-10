# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import logging
import time
import re
import csv
import CommonFunctions as cf


from datetime import datetime

pudonglist = ["beicai", "biyun", "caolu", "chuansha", "datuanzhen", "gaodong",
                "gaohang", "geqing", "hangtou", "huamu", "huinan",
                "jinqiao", "jinyang", "kangqiao", "laogangzhen",
                "lianyang", "lingangxincheng", "lujiazui", "nanmatou",
                "nichengzhen", "sanlin", "shibo", "shuyuanzhen",
                "tangqiao", "tangzhen", "waigaoqiao", "wanxiangzhen",
                "weifang", "xinchang", "xuanqiao", "yangdong",
                "yangjing", "yuanshen", "yuqiao1", "zhangjiang", "zhoupu", "zhuqiao"]

def handlelinks1(pageUrl):

    html = getresponsefromurl(pageUrl)
    bsObj = BeautifulSoup(html.content, 'lxml')

    price = bsObj.find("div", {"class": "price"})
    price = findStr(u'<span class=\"total\">', str(price), u'</span')

    unitPrice = bsObj.find("div", {"class": "unitPrice"})
    unitPrice = findStr(u'<span class=\"unitPriceValue\">', str(unitPrice), u'<i>')

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

    return [area, position, communityName, circlearea, price, unitPrice, room, areas, floor, huxing, orientation,
            elavatorRate, decorate, duration, structure, elavator, bighousetype, pageUrl]


def handlelinks(pageUrl):
    html = cf.getresponsefromurl(pageUrl)
    bsObj = BeautifulSoup(html.content, 'lxml')

    price = bsObj.find("span", {"class": "xiaoquUnitPrice"}).string
    logging.info(price)

    xiaoquInfo = bsObj.find("div", {"class": "xiaoquInfo"})
    for child in xiaoquInfo.children:
        if child.find("span", {"class": "xiaoquInfoLabel"}).string == '开发商':
            kaifangshang = child.find("span", {"class": "xiaoquInfoContent"}).string
            logging.info(kaifangshang)
        elif child.find("span", {"class": "xiaoquInfoLabel"}).string == '建筑年代':
            jianzhuniandai = child.find("span", {"class": "xiaoquInfoContent"}).string
            logging.info(jianzhuniandai)
        elif child.find("span", {"class": "xiaoquInfoLabel"}).string == '建筑类型':
            jianzhuleixing = child.find("span", {"class": "xiaoquInfoContent"}).string
            logging.info(jianzhuleixing)
        elif child.find("span", {"class": "xiaoquInfoLabel"}).string == '物业费用':
            wuyefeiyong = child.find("span", {"class": "xiaoquInfoContent"}).string
            logging.info(wuyefeiyong)
        elif child.find("span", {"class": "xiaoquInfoLabel"}).string == '物业公司':
            wuyegongsi = child.find("span", {"class": "xiaoquInfoContent"}).string
            logging.info(wuyegongsi)
        elif child.find("span", {"class": "xiaoquInfoLabel"}).string == '楼栋总数':
            loudongzongshu = child.find("span", {"class": "xiaoquInfoContent"}).string
            logging.info(loudongzongshu)
        elif child.find("span", {"class": "xiaoquInfoLabel"}).string == '房屋总数':
            fangwuzongshu = child.find("span", {"class": "xiaoquInfoContent"}).string
            logging.info(fangwuzongshu)

    return [price, kaifangshang, jianzhuniandai, jianzhuleixing, wuyefeiyong,
            wuyegongsi, loudongzongshu, fangwuzongshu]


    # unitPrice = bsObj.find("div", {"class": "unitPrice"})
    # unitPrice = cf.findStr(u'<span class=\"unitPriceValue\">', str(unitPrice), u'<i>')
    #
    # # aroundInfo = bsObj.find("div", {"class": "aroundInfo"})
    # # logging.info(aroundInfo)
    #
    # try:
    #     g = bsObj.find("div", {"class": "communityName"}).stripped_strings
    #     communityName = ''
    #     logging.info(next(g))
    #     communityName = next(g)
    # except Exception as e:
    #     logging.info('Exception in get communityName:', e.value)
    #
    # try:
    #     g = bsObj.find("div", {"class": "areaName"}).stripped_strings
    #     area = ''
    #     position = ''
    #     circlearea = ''
    #     logging.info(next(g))
    #     area = next(g)
    #     position = next(g)
    #     circlearea = next(g)
    # except Exception as e:
    #     logging.info('Exception in get areaName:', e.value)
    #
    # introContent = bsObj.find("div", {"class": "introContent"})
    # room = cf.findStr(u'房屋户型</span>', str(introContent), u'</li>')
    # floor = cf.findStr(u'所在楼层</span>', str(introContent), u'</li>')
    # areas = cf.findStr(u'建筑面积</span>', str(introContent), u'</li>')
    # huxing = cf.findStr(u'户型结构</span>', str(introContent), u'</li>')
    # orientation = cf.findStr(u'房屋朝向</span>', str(introContent), u'</li>')
    # structure = cf.findStr(u'建筑结构</span>', str(introContent), u'</li>')
    # decorate = cf.findStr(u'装修情况</span>', str(introContent), u'</li>')
    # elavatorRate = cf.findStr(u'梯户比例</span>', str(introContent), u'</li>')
    # elavator = cf.findStr(u'配备电梯</span>', str(introContent), u'</li>')
    # duration = cf.findStr(u'产权年限</span>', str(introContent), u'</li>')
    # bighousetype = cf.findStr(u'别墅类型</span>', str(introContent), u'</li>')
    #
    # # aroundInfo = bsObj.find("div", {"class": "transaction"})
    # # logging.info(aroundInfo)
    # # starttosell = findStr(u'挂牌时间</span><span>', str(introContent), u'</li>')
    # # housetype = findStr(u'交易权属</span><span>', str(introContent), u'</li>')
    # # lasttrade = findStr(u'上次交易</span><span>', str(introContent), u'</li>')
    # # indexNo = findStr(u'房源编号：', str(aroundInfo), u'</span>')
    #
    # return [area, position, communityName, circlearea, price, unitPrice, room, areas, floor, huxing, orientation,
    #         elavatorRate, decorate, duration, structure, elavator, bighousetype, pageUrl]


if __name__ == '__main__':
    cf.initlogging("Test-%s.log" % datetime.now().strftime('%Y%m%d-%H%M%S'))
    logging.info('start main process')

    # url = " https://sh.lianjia.com/ershoufang/107101243278.html"
    # estateContent = handlelinks1(url)
    # logging.info(estateContent)

    url = "https://sh.lianjia.com/xiaoqu/5011000018330/"
    handlelinks(url)



