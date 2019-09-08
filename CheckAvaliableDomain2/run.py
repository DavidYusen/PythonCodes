# encoding:utf-8

import os


def generate_list():
    wlist='abcdefghijklmnopqrst'
    urlist=[m + n + o for m in wlist for n in wlist for o in wlist]
    return urlist


def generate_list1():
    urlist = ['abc','bcd','adfed','aaaaaa99d9998']
    return urlist


urllist = generate_list()
f = open("result.txt", 'w')

for urlitem in urllist:
    cmd = "nslookup www.%s.com" % urlitem
    with os.popen(cmd, "r") as p:
        result = p.read()

    if urlitem not in result:
        f.write(urlitem)
        f.write('\n')
f.close()
