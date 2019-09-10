# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from datetime import datetime
import logging
import time
import re
import csv
import CommonFunctions as cf

pudonglist = ["beicai", "biyun", "caolu", "chuansha", "datuanzhen", "gaodong",
                "gaohang", "geqing", "hangtou", "huamu", "huinan",
                "jinqiao", "jinyang", "kangqiao", "laogangzhen",
                "lianyang", "lingangxincheng", "lujiazui", "nanmatou",
                "nichengzhen", "sanlin", "shibo", "shuyuanzhen",
                "tangqiao", "tangzhen", "waigaoqiao", "wanxiangzhen",
                "weifang", "xinchang", "xuanqiao", "yangdong",
                "yangjing", "yuanshen", "yuqiao1", "zhangjiang", "zhoupu", "zhuqiao"]
# pudonglist = ["biyun", "caolu"]


def handlelinks(pageUrl):
    html = cf.getresponsefromurl(pageUrl)
    bsObj = BeautifulSoup(html.content, 'lxml')

    try:
        name = bsObj.find("h1", {"class": "detailTitle"})
        if name is not None:
            name = name.string
        else:
            name = ''
    except Exception as e:
        logging.info("Exception in getting name")
        name = ''

    try:
        address = bsObj.find("div", {"class": "detailDesc"})
        if address is not None:
            address = address.string
        else:
            address = ''
    except Exception as e:
        logging.info("Exception in getting address")
        address = ''

    try:
        price = bsObj.find("span", {"class": "xiaoquUnitPrice"})
        if price is not None:
            price = price.string
        else:
            price = ''
    except Exception as e:
        logging.info("Exception in handling unit price")
        price = ''

    xiaoquInfo = bsObj.find("div", {"class": "xiaoquInfo"})
    kaifangshang = ''
    jianzhuniandai = ''
    jianzhuleixing = ''
    wuyefeiyong = ''
    wuyegongsi = ''
    loudongzongshu = ''
    fangwuzongshu = ''

    if xiaoquInfo is None:
        logging.info("Failed handing " + url)
        return [name, address, price]
    else:
        for child in xiaoquInfo.children:
            if child.find("span", {"class": "xiaoquInfoLabel"}).string == '开发商':
                kaifangshang = child.find("span", {"class": "xiaoquInfoContent"}).string
            elif child.find("span", {"class": "xiaoquInfoLabel"}).string == '建筑年代':
                jianzhuniandai = child.find("span", {"class": "xiaoquInfoContent"}).string
            elif child.find("span", {"class": "xiaoquInfoLabel"}).string == '建筑类型':
                jianzhuleixing = child.find("span", {"class": "xiaoquInfoContent"}).string
            elif child.find("span", {"class": "xiaoquInfoLabel"}).string == '物业费用':
                wuyefeiyong = child.find("span", {"class": "xiaoquInfoContent"}).string
            elif child.find("span", {"class": "xiaoquInfoLabel"}).string == '物业公司':
                wuyegongsi = child.find("span", {"class": "xiaoquInfoContent"}).string
            elif child.find("span", {"class": "xiaoquInfoLabel"}).string == '楼栋总数':
                loudongzongshu = child.find("span", {"class": "xiaoquInfoContent"}).string
            elif child.find("span", {"class": "xiaoquInfoLabel"}).string == '房屋总数':
                fangwuzongshu = child.find("span", {"class": "xiaoquInfoContent"}).string

        logging.info("Finish handing " + url)
        return [name, address, price, kaifangshang, jianzhuniandai, jianzhuleixing, wuyefeiyong,
                wuyegongsi, loudongzongshu, fangwuzongshu, pageUrl]


if __name__ == '__main__':

    cf.initlogging("Main-%s.log" % datetime.now().strftime('%Y%m%d-%H%M%S'))
    logging.info('start main process')
    url = "https://sh.lianjia.com/xiaoqu/"
    FILE_BOJECT = open("%s.csv" % datetime.now().strftime('%Y%m%d-%H%M%S'), "a", newline='')
    writer = csv.writer(FILE_BOJECT)

    for district in pudonglist:
        communitypages = set()
        logging.info("start handling district: " + district)
        districturl = url + district + '/'
        req = cf.getresponsefromurl(districturl)
        soup = BeautifulSoup(req.content, 'lxml')
        communitycount = int(soup.find_all(class_="total fl")[0].span.string)
        pagecount = communitycount // 30 + 1
        logging.info("district " + district + " , " + "community count:" + str(communitycount))

        for page in range(1, pagecount+1):
            newurl = districturl + 'pg' + str(page)
            req = cf.getresponsefromurl(newurl)
            soup = BeautifulSoup(req.content, "lxml")
            logging.info('handling directory page ' + str(page))
            linkList = soup.findAll(href=re.compile("xiaoqu\/[0-9]"))
            logging.info(len(linkList))
            for link in linkList:
                if 'href' in link.attrs:
                    if link.attrs['href'] not in communitypages:
                        newPage = link.attrs['href']
                        communitypages.add(newPage)
                        logging.info('Find new community: ' + newPage)

        for page in communitypages:
            logging.info('start handling: ' + page)
            communityContent = handlelinks(page)
            writer.writerow(communityContent)
            time.sleep(0.1)
            # logging.info('Done.')

    logging.info("Get community info is done.")
