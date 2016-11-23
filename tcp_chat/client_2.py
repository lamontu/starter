# -*- coding: utf-8 -*-

import socket


s = socket.socket()
host = '192.168.2.106'
port = 12345
s.connect((host, port))
print('Linked')
info = s.recv(1024).decode('utf-8')
while info != 'exit':
    print("From others: " + info)
    send_mes = input('send message: ')
    s.send(send_mes.encode('utf-8'))
    if send_mes == 'exit':
        break
    info = s.recv(1024).decode('utf-8')
s.close()


