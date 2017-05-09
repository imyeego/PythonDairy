#!/usr/bin/python
# _*_ coding:utf-8 _*_

import string
import b
i =raw_input('请输入一个数字：')

print b.abs(string.atof(i) if b.isContains(i, '.') else int(i))