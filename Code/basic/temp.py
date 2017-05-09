#!/usr/bin/python
# _*_ coding:utf-8 _*_

#str = 'apple watch is beautiful!'
#list1 = [1,3,51,'liu',6,3.14]

#list2 = list(str)    #字符串转list

#tup = (1, 2, 5, 9, 1.5, 'python')  #tuples与list的区别：tuples不可修改
#i = 0
#print 'readline'

print 'readlines'
list3 = open('Python_loop.py', 'r').readlines()
for c in list3:
	print c,
	#i = i + 1
else:
	print 'out readlines'
print len(list3)

for r in open('Python_loop.py', 'r').readlines():
	open('temp.py', 'a+').write(r)