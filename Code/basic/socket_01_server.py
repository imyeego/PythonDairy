#!/usr/bin/python
# _*_ coding:utf-8 _*_
import socket    #socket模块
import commands		#执行系统命令模块

HOST = 'localhost'
PORT = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	#定义socket类型，网络通信，TCP
s.bind((HOST, PORT))	#套接字绑定的IP与端口

s.listen(1)		#开始监听

while True:
	conn, addr = s.accept()
	print 'Connect by', addr
	while 1:
		data = conn.recv(1024)
		cmd_status, cmd_result = commands.getstatusoutput(data)
		if len(cmd_result.strip()) == 0:
			conn.sendall('Done.')
		else:
			conn.sendall(cmd_result)

conn.close()	#关闭连接



