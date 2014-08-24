#!/usr/bin/python
#codeing=utf-8
#Filename:socketServer.py

import socket
s = socket.socket()#get the socket

host = socket.gethostname()# get host
port = 1234 #select a port
s.bind((host,port))# build a bind

s.listen(5)# start listen,5 imply there will be at most 5 client
while True:
	#s.accept will return a (socket,address)
	clientSocket,addr=s.accept()
	print 'Got connect from',addr
	clientSocket.send('Thank you for connecting!')
	clientSocket.close()
