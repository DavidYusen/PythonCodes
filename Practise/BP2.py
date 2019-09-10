# -*- coding: utf-8 -*-


tl = [42, 38, 'HongKong', 'Jimmy', [9, 4, 23, -3, 'Stock']]

print(tl[0])
print(len(tl))

tl.append(34)
tl.append('34')

tl.extend([12, 98, 'mnk'])
tl.insert(3, 55)

ml = tl.copy()

print(ml)

# list 很适合用作栈，后进先出，但不适合用作queue
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)
print(stack.pop())
print(stack.pop())

# # 格式化输出日期的demo
# months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
# dayendings = ['st', 'nd', 'rd'] + 17 * ['th'] + ['st', 'nd', 'rd'] + 7 * ['th'] + ['st']
# year = input('Year: ')
# monthnumber = int(input('Month(1-12): '))
# daynumber = int(input('Day (1-31: '))
# print(months[monthnumber-1], str(daynumber) + dayendings[daynumber-1], year)

numbers = [x for x in range(20)]
n1 = numbers[:: 2]
n2 = numbers[:: 3]
print(n1+n2)
