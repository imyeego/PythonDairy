#!/usr/bin/python
# _*_ coding:utf-8 _*_

def add(val1, val2):
	return val1 + val2

def pow_a(f1, f2):
	return f1**f2

def subtract(f1, f2):
	return f1 - f2

#temp = add(15 ,20)
#temp1 = pow_a(3, 4)

# print '相加',temp
# print '指数',temp1
# print '相减',subtract(120, 45)

def isadult():
	if int(raw_input("输入你的年龄:")) >= 18:
		print '你已成年。'
	else:
		print '你未成年。'

def buttom_score():
	count = int(raw_input("输入你的分数"))
	if count >= 60:
		if count >= 70:
			if count >= 80:
				if count >= 90:
					print 'A'
				else:
					print 'B'
			else:
				print 'C'
		else:
			print 'D'
	else:
		print '不及格'



def score():
	count = int(raw_input("输入你的分数："))
	if count < 60:
		print '不及格'
	else:
		if count < 70:
			print 'D'
		else:
			if count < 80:
				print 'C'
			else:
				if count < 90:
					print 'B'
				else:
					print 'A'

def top_score():
	count = int(raw_input("输入你的分数："))

	if count < 60:
		print '不及格'
	elif count < 70:
		print 'D'
	elif count < 80:
		print 'C'
	elif count < 90:
		print 'B'
	else:
		print 'A'

top_score()






