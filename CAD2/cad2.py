# encoding:utf-8

import os


def generate_list():
    urllist = []
    f1 = open('chnlist.txt', 'r')
    for x in f1.readlines():
        urllist.append(x.replace("\n", ""))
    resultlist = [m + n for m in urllist for n in urllist]
    return resultlist


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
