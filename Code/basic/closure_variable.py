#coding:utf-8
'''
Theme: closure of python with enclosing variable
Author: Zhao Liu <imyeego@gmail.com>
'''
passline = 60 #global
'''
def func(val): #
	print ('%x'%id(val))
	if val >= passline:
		print ('pass')
	else:
		print ('failed')
	def in_func():
		print (val)

	return in_func
'''
def setpassline(passline):
	def compute(val):
		if val >= passline:
			print ('pass')
		else:
			print ('failed')

	return compute
#f_150 = setpassline(150)
#f_100(67)
f_100 = setpassline(100)
f_100(67)
