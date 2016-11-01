# -*- coding: utf-8 -*-

import socket


# Address
HOST = ''
PORT = 8000

# Prepare HTTP response
# start line, message head, message body
# a blank line between message head and message body
text_content = '''HTTP/1.x 200 OK     
Content-Type: text/html

<html>
<head>
    <title>WOW</title>
</head>
<body>
    <p>Wow, Python Server</p>
    <IMG src="http_server_img.jpg"/>
    <form name="input" action="/" method="post">
        First name:<input type="text" name="firstname"><br>
        <input type="submit" value="Submit">
    </form>
</body>
</html>
'''

# Read picture, put into HTTP format
# start line, head, body, a blank line between head and body
f = open('http_server_img.jpg', 'rb')
pic_content = '''HTTP/1.x 200 OK
Content-Type: image/jpg

'''

#pic_content = bytes(pic_content + str(f.read()), 'utf-8')
pic_content  = pic_content.encode('utf-8') + f.read()
f.close()


# Configure socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

# infinite loop, server forever
while True:
    # 3: maximum number of requests waiting
    s.listen(3)
    conn, addr = s.accept()
    request = conn.recv(1024).decode('utf-8')  # 1024: receiving buffer size
    method = request.split(' ')[0] 
    src = request.split(' ')[1]
   
    # deal with GET method
    if method == 'GET':
        # URL
        if src == '/http_server_img.jpg':
            content = pic_content
        else:
            content = text_content.encode('utf-8')    

        print('Connected by', addr)
        print('Request is:', request)
        conn.sendall(content)
    
    if method == 'POST':
        form = request.split('\r\n')
        idx = form.index('')
        entry = form[idx:]

        value = entry[-1].split('=')[-1]
        text_content = text_content + '\n <p>' + value + '</p>'
        content = text_content.encode('utf-8')
        conn.sendall(content)


    # close connection
    conn.close()


