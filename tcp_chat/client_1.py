# -*- coding: utf-8 -*_

import socket


host = '192.168.2.106'
port = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

print(s.recv(1024).decode('utf-8'))
for data in ['Michael', 'Tracy', 'Sarah']:
    s.send(data.encode('utf-8'))
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()


