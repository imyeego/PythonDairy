#!/usr/bin/python
# _*_ coding:utf-8 _*_

# 变量交换

from collections import Counter

x = 5
y = 6
x, y = y, x
print x, y

#if语句在行内

print "Hello" if True else "World"

#除后向下取整

print 7.0//3
# 2的5次方
print 2**5

#浮点数的除法
.3/.2	#等价于3.0/2.0

#数值比较
x = 2
if 4 > x > 1:
	print x

if 1 < x > 0:
	print x

#初始化列表的值
item = [0]*3

#Counter函数统计字符串中每个字符的个数
print Counter("facebook")







