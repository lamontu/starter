# -*- coding: utf-8 -*-

import socketserver


HOST = ''
PORT = 8000

text_content = '''
HTTP/1.x 200 OK
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

text_content = bytes(text_content, 'utf-8')

f = open('http_server_img.jpg', 'rb')
pic_content = '''
HTTP/1.x 200 OK
Content-Type: image/jpg

'''

pic_content = bytes(pic_content, 'utf-8') + f.read()
f.close() 


# This class defines response to each request
class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        # self.request is the TCP socket connected to the client
        request = self.request.recv(1024).decode('utf-8')

        print('Connected by', self.client_address[0])
        print('Request is', request)
       
        method = request.split(' ')[0]
        src = request.split(' ')[1]
        
        global text_content

        if method == 'GET':
            if src == '/http_server_img.jpg':
                content = pic_content
            else:
                content = text_content
            self.request.sendall(content)
        
        if method == 'POST':
            form = request.split('\r\n')
            idx = form.index('')
            entry = form[idx:]

            value = entry[-1].split('=')[-1]
            text_content = str(text_content) + '\n <p>' + value + '</p>'
            content = text_content.encode('utf-8')
            self.request.sendall(content)
            
            """ 
            # More operations, such as put the form into database
            """ 


# Create the server
server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)

# Start the server, and work forever
server.serve_forever()

 
