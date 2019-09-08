from string import capwords
from string import ascii_lowercase

print(capwords("abc,dedf,sdfe,ss", ","))
print(ascii_lowercase)


aDict = {'host': 'earth'}
aDict['port'] = 80
print(aDict['host'])
print(dir(aDict))


# 装饰器的例子

def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


@log
def now():
    print("2018-3-28")

# 把@log放到now()函数的定义处，相当于执行了语句：now = log(now)
# 由于log()是一个decorator，返回一个函数，所以，原来的now()函数仍然存在，
# 只是现在同名的now变量指向了新的函数，于是调用now()将执行新函数，
# 即在log()函数中返回的wrapper()函数。



f = now
f()

print(now.__name__)
print(f.__name__)


def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


def trim(s):
    while s[:1] == ' ':
        s = s[1:]
    while s[-1:] == ' ':
        s = s[:-1]
    return s


# 测试:
if trim('hello  ') != 'hello':
    print('测试失败1!')
elif trim('  hello') != 'hello':
    print('测试失败2!')
elif trim('  hello  ') != 'hello':
    print('测试失败3!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败4!')
elif trim('') != '':
    print('测试失败5!')
elif trim('    ') != '':
    print('测试失败6!')
else:
    print('测试成功!')


# for循环
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)

for ch in 'ABC':
    print(ch)

# 通过collections模块的Iterable类型判断对象是否可迭代
from collections import Iterable
print(isinstance('abcd', Iterable))

# 通过enumerate函数可以把一个list变成索引-元素对，实现下标循环
for i, value in enumerate('abc'):
    print(i, value)