#/usr/bin/python
#-*- Coding:utf-8 -*-

def abs(i):
	return i if i > 0 else -i
	#return i > 0 and i or -i

def isContains(str, a):
	return True if a in str else False

if __name__ == "__main__":
	print abs(-15)