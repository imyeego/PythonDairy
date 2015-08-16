import socket

address = ('localhost', 8888)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
	msg = raw_input("Type something:")
	if not msg:
		break
	s.sendto(msg,address)
s.close()