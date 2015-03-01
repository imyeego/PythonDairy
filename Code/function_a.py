#!/usr/bin/python
# _*_ coding:utf-8 _*_

import sys
def add(val1, val2):
	return val1 + val2

def pow_a(f1, f2):
	return f1**f2

def subtract(f1, f2):
	return f1 - f2

temp = add(15 ,20)
temp1 = pow_a(3, 4)

print sys.getdefaultencoding()
print '相减',temp1
print 'subtract',subtract(120, 45)
