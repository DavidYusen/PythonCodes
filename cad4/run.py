# encoding:utf-8

import os


def generate_list3():
    urllist = []
    f1 = open('words.txt', 'r')
    for x in f1.readlines():
        urllist.append(x.replace("\n", ""))
    return urllist

def generate_list4():
    wlist='abcdefghijklmnopqrst'
    urlist = [m + n + o + x + q for m in wlist for n in wlist for o in wlist for x in wlist for q in wlist]
    return urlist


def generate_list1():
    urlist = ['abc','bcd','adfed','aaaaaa99d9998']
    return urlist


# urllist = generate_list()
# f = open("temp.txt", 'w')
# #
# # for urlitem in urllist:
# #     cmd = "nslookup www.%s.com" % urlitem
# #     with os.popen(cmd, "r") as p:
# #         result = p.read()
# #
# #     if urlitem not in result:
# #         f.write(urlitem)
# #         f.write('\n')
# # f.close()

f1 = open("temp.txt", 'r')
f2 = open("result.txt", 'w')

for line in f1.readlines():
    if len(line) < 10:
        f2.write(line)

f1.close()
f2.close()
