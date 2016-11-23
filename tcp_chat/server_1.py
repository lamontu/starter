# -*- coding: utf-8 -*-

import socket
import time
import threading


def tcplink(sock, addr):
    print("Accept new connection from %s:%s..." % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if data == 'exit' or not data:
            break
        sock.send(b"Hello, %s!" % data)
    sock.close()
    print("Connection from %s:%s closed." % addr)


host = ''
port = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(5)
while True:
    sock, addr = s.accept()
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()


