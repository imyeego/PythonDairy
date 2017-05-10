# encoding:utf-8
'''
Author: Zhao Liu <imyeego@gmail.com>
Theme: using of python decorator

'''
def dec(func):
	def in_dec(*arg):
		if len(arg) == 0:
			return 0
		for val in arg:
			if not isinstance(val, int):
				return 0
		return func(*arg)
	return in_dec

@dec
def my_sum(*arg):
	return sum(arg)
@dec
def my_average(*arg):
	return sum(arg) / len(arg)

print (my_sum(1,2,3,4,5,6))
print (my_average('1',2,3,4))
print (my_average(1,2,3,4,5,6))