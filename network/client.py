# -*- coding: utf-8 -*-

import socket


# Address
HOST = '192.168.2.106'  # using ifconfig to check the correct ip
PORT = 8000

request = bytes('can you hear me?', 'utf-8')

# configure socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# send message
s.sendall(request)

# receive message
reply = s.recv(1024)
print('reply is:', reply)

# close connection
s.close()


