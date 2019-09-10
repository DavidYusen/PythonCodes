# -*- coding: utf-8 -*-


from math import pi
import string
from string import Template

# string格式化打印
format1 = "Hello, %s. %s enough for ya?"
values = ('world', 'Hot')
print(format1 % values)

format2 = "Pi with three decimal: %.5f"
print(format2 % pi)

# 使用string模板
s1 = Template('$x, glorious $x!')
s2 = s1.substitute(x='slurm')
print(s2)

width = 35
price_width = 10
item_width = width - price_width

print('=' * width)
header_format = '%-*s%*s'
print(header_format % (item_width, 'Item', price_width, 'Price'))
print('-' * width)

body_format = '%-*s%*.2f'
print(body_format % (item_width, 'Apples', price_width, 0.4))
print(body_format % (item_width, 'Pears', price_width, 0.6))
print(body_format % (item_width, 'Oranges', price_width, 1.3))
print(body_format % (item_width, 'Prunes(4 lbs.)', price_width, 12))

print(string.digits)

title = 'Show me THE meaning of being lonely'
print(title.find('being'))
print(title.find('me'))
print(title.lower())
print(title.title())
print(string.capwords(title))
print(title.replace('me', 'us').title())

tlist = title.split(' ')
print(tlist)
