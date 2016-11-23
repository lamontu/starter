# -*- coding: utf-8 -*-

import socket


host = ''
port = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)

sock, addr = s.accept()
print('Linked')
sock.send(b'I am a server, welcome!')
info = sock.recv(1024).decode('utf-8')
while info != 'exit':
    print("From others: " + info)
    send_mes = input("send message: ")
    sock.send(send_mes.encode('utf-8'))
    if send_mes == 'exit':
        break
    info = sock.recv(1024).decode('utf-8')
sock.close()
s.close()


