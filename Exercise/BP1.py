# -*- coding: utf-8 -*-

import math
import cmath

data = ['ACE', -9, 18, 28, 10.7]
e, a, b, c, d = data
print(a, b, c)

# 两种开根方法的区别
print(cmath.sqrt(a))
print(cmath.sqrt(b))
print(math.sqrt(b))

# 乘方的两种计算方法
print(2**3)
print(pow(2, 3))

# python3没有raw_input了，只有input，接受任意输入, 将输入默认为字符串处理,并返回字符串类型
# name = input("What is your name? ")
# print('Hello, ' + name + '!')
# print(type(name))
# age = input("How old are you ")
# print('Welcome, ' + age + ' year old boy!')
# print(type(age))

# 取整的三种方法
x = 38.478
print(type(math.ceil(x)))
print(math.ceil(x))
print(math.floor(x))
print(round(x))

# repr：返回一个对象的string格式
s = 'RUNOOB'
print(repr(s))
