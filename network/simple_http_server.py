# -*- coding: utf-8 -*

import socketserver
import http.server


HOST = ''
PORT = 8000


# Create the server, SimpleHTTPRequestHandler is pre-defined in http.server
server = socketserver.TCPServer((HOST, PORT), 
                                 http.server.SimpleHTTPRequestHandler)
# Start the server
server.serve_forever()


