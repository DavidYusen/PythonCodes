# -*- coding: utf-8 -*-

import logging
import requests
import time


def initlogging(logfilename):
    logging.basicConfig(filename=logfilename,
                        filemode="w",
                        format="%(asctime)s %(name)s:%(levelname)s:%(message)s",
                        datefmt="%d-%m-%Y %H:%M:%S",
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
    rtnStr = ''

    if startLoc != -1:
        startLoc = orgStr.find(startStr) + len(startStr)
    else:
        return rtnStr

    endLoc = orgStr.find(endStr, startLoc)
    if startLoc != -1 and endLoc != -1:
        rtnStr = orgStr[startLoc:endLoc].strip()

    return rtnStr
