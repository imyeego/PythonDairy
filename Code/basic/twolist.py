#!/usr/bin/python
# _*_ coding:utf-8 _*_

#同时遍历两个列表
l1 = ['liuzhao','zhangfen']
l2 = ['lilei','wanggang']

for i1, i2 in zip(l1, l2):
	print i1 + ' vs. ' + i2

#带索引的列表迭代

l3 = ['apple','google','microsoft','amazon','facebook','yahoo']
for index, i in enumerate(l3):
	print index, i

#列表推导式
#已知一个列表，筛选出偶数列表的方法：
numbers = [1,2,3,4,5,6,7,8,9,10]
even = [number for number in numbers if number%2 == 0]
print even

#FizzBuzz
#写一个程序，打印数字1到100，3的倍数打印“Fizz”来替换这个数，5的倍数打印“Buzz”，
#对于既是3的倍数又是5的倍数的数字打印“FizzBuzz”
for x in range(101):
	print "fizz"[x%3*4::] + "buzz"[x%5*4::] or x,