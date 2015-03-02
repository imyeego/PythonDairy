#!/usr/bin/python
# _*_ coding:utf-8 _*_

''' 布尔表达式，只要不为0或false，就为真

if True:
	print 'True'
else:
	print 'False'


if 0:
	print 'True'
else:
	print 'False'

if 4:				# 非0即真
	print 'True'
else:
	print 'False'


if -5:				# 非0即真，无论正负
	print 'True'
else:
	print 'False'

if 'liuzhao':				# 字符串为真
	print 'True'
else:
	print 'False'

'''
# 关系表达式

sex = raw_input('输入你的性别：')

if not sex == 'male' or sex == 'boy':  # 注意其结合性与优先级
	print 'Man'
else:
	print 'Woman'





















