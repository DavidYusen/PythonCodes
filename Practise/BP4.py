# -*- coding: utf-8 -*-
from datetime import datetime

#
# age = 1
# assert 0 < age < 100, 'The age must be realistic'
#
#
# def get_sunday():
#     print('It is Sunday')
#
#
# def get_monday():
#     print('It is Monday')
#
#
# def get_tuesday():
#     print('It is Tuesday')
#
#
# def get_default():
#     return 'Unkown'
#
#
# TCSwticher = {
#     0: get_sunday,
#     1: get_monday,
#     2: get_tuesday
# }
#
# TC = 2
#
# TCSwticher.get(TC, get_default)()
# TCSwticher[TC]()

#
# people = {
#     'Alice': {
#         'phone': '2341',
#         'addr': 'Foo drive 23'
#     },
#
#     'Beth': {
#         'phone': '9102',
#         'addr': 'Bar street 42'
#     },
#
#     'Cecil': {
#         'phone': '3158',
#         'addr': 'Baz avenue 90'
#     }
# }
#
# lables = {
#     'phone': 'phone number',
#     'addr': 'address'
# }
#
# name = input('Name: ')
# request = input('Phone number or address?')
#
# if request == 'p':
#     key = 'phone'
#
# if request == 'a':
#     key = 'addr'
#
# if name in people:
#     print("%s %s is %s." % (name, lables[key], people[name][key]))

d = {}
d['name'] = 'Gumby'
d['age'] = 42
print(d)
p = d
p.clear()
print(d)
print(d.get('test', 'None'))

d3 = {'x': 1, 'y': 2, 'z': 3}
for key, value in d3.items():
    print(key, 'corresponds to ', value)
