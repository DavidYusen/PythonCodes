import logging
from math import sqrt

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S')

logger = logging.getLogger(__name__)


def exe4():
    iyear = int(input("please input the year:"))
    imonth = int(input("please input the month:"))
    iday = int(input("please input the day:"))

    months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)

    if 0 < imonth < 12:
        sum = months[imonth-1]
    else:
        print('data error')

    sum += iday

    if(iyear % 400 == 0) or ((iyear % 4 == 0) and (iyear % 100 != 0)):
        leap = 1
    else:
        leap = 0

    if (leap == 1) and (imonth > 2):
        sum += 1

    print('it is the %dth day.' % sum)


def exe3():
    x = 1
    while x < 10000:
        x1 = sqrt(x + 100) - int(sqrt(x + 100))
        x2 = sqrt(x + 268) - int(sqrt(x + 268))
        if x1 == 0 and x2 == 0:
            print(x)
        x += 1


def exe2a():
    x = int(input("Please input the profit:"))
    if x <= 100000:
        result = x*0.1
    elif x <= 200000:
        result = 100000*0.1 + (x-100000)*0.075
    elif x <= 400000:
        result = 100000*0.1 + 100000*0.075 + (x-200000)*0.05
    elif x <= 600000:
        result = 100000*0.1 + 100000*0.075 + 200000*0.05 + (x-400000)*0.03
    elif x <= 1000000:
        result = 100000*0.1 + 100000*0.075 + 200000*0.05 + 200000*0.03 + (x-600000)*0.015
    else:
        result = 100000*0.1 + 100000*0.075 + 200000*0.05 + 200000*0.03 + 400000*0.015 + (x-1000000)*0.01

    return result


def exe2b():
    x = int(input("Please input the profit:"))
    arr = [1000000, 600000, 400000, 200000, 100000, 0]
    rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
    r = 0
    for idx in range(0, len(arr)):
        if x > arr[idx]:
            r += (x-arr[idx])*rat[idx]
            x = arr[idx]
    return r


def exe1():
    nums1 = [1, 2, 3, 4]

    for i in nums1:
        for j in nums1:
            for k in nums1:
                if k != i and k != j and i != j:
                    print(j * 100 + i * 10 + k)


if __name__ == '__main__':
    exe4()
