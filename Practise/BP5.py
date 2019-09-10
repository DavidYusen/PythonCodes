# -*- coding: utf-8 -*-


names = ['anne', 'beth', 'george', 'damon']
ages = [12, 35, 53, 23]
for i in range(len(names)):
    print('%s is %s years old' % (names[i], ages[i]))

for name, age in zip(names, ages):
    print('This year, %s is %s years old' % (name, age))

list1 = [(x, y) for x in range(10) if x % 3 == 0 for y in range(3)]
print(list1)

girls = ['alice', 'bernice', 'clarice']
boys = ['chris', 'arnold', 'bob']
list2 = [b+'+'+g for b in boys for g in girls if b[0] == g[0]]
print(list2)

letterGirls = {}
for girl in girls:
    letterGirls.setdefault(girl[0], []).append(girl)

print(b+'+'+g for b in boys for g in letterGirls[b[0]])