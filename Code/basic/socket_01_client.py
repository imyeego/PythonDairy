#!/usr/bin/python
# _*_ coding:utf-8 _*_

import socket

port = 8888
host = 'localhost'
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host, port))

while True:
	cmd = raw_input('please input cmd:')	#与人交互，输入命令
	s.sendall(cmd)
	data = s.recv(1024)
	print data
s.close()