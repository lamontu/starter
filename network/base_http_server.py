# -*- coding: utf-8 -*-

import http.server


HOST = ''
PORT = 8000


# Create the server, CGIHTTPRequestHandler is pre-defined in http.server
server = http.server.HTTPServer((HOST, PORT),
                                 http.server.CGIHTTPRequestHandler)
# Start the server
server.serve_forever()


