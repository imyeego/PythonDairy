import socket

address = ('localhost',8888)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(address)

while True:
	data, addr = s.recvfrom(2048)
	if not data:
		print 'Client has exist'
		break
	print "received:",data,"from", addr
s.close()