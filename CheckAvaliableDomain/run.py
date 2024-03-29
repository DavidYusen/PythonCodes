# encoding:utf-8

import os


# 从文件中读取每行的字符串作为域名
def generate_list():
    urllist = []
    f1 = open('words.txt', 'r')
    for x in f1.readlines():
        urllist.append(x.replace("\n", ""))
    return urllist


# 生成任意三个字母组合的域名
def generate_list1():
    wlist = 'abcdefghijklmnopqrst'
    urlist = [m + n + o for m in wlist for n in wlist for o in wlist]
    return urlist


# 任两个字符串的组合作为域名
def generate_list2():
    urllist = []
    f1 = open('chnlist.txt', 'r')
    for x in f1.readlines():
        urllist.append(x.replace("\n", ""))
    resultlist = [m + n for m in urllist for n in urllist]
    return resultlist


if __name__ == '__main__':
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
