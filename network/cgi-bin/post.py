#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi


form = cgi.FieldStorage()

# Output to stdout, CGIHttpServer will take this as response to the client
print("Content-Type: text/html")
print()
print("<p>Hello world!</p>")
print("<p>" + repr(form['firstname']) + "</p>")


