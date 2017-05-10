# encoding:utf-8
'''
Author: Zhao Liu <imyeego@gmail.com>
Theme: closure of python with enclosing function

'''

def my_sum(*arg):
	return sum(arg)

def my_average(*arg):
	return sum(arg) / len(arg)

def dec(func):
	def in_dec(*arg):
		if len(arg) == 0:
			return 0
		for val in arg:
			if not isinstance(val, int):
				return 0
		return func(*arg)
	return in_dec

_my_sum = dec(my_sum)
_my_average = dec(my_average)

print (_my_sum(1,2,3,4,5,6))
print (_my_average('1',2,3,4))
print (_my_average(1,2,3,4,5,6))