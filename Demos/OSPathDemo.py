import os

# __file__ 是用来获得模块所在的路径的，可能得到的是一个相对路径，也可能是绝对路径，取决于执行脚本的命令
print(__file__)

# os.path.realpath: 获取当前当前文件的绝对路径
print(os.path.realpath(__file__))

# os.path.dirname： 获取当前文件上一层目录
print(os.path.dirname(os.path.realpath(__file__)))
