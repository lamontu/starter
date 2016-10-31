# -*- coding: utf-8 -*-

import sqlite3


conn = sqlite3.connect('test.db')
c = conn.cursor()


c.execute('SELECT name FROM category ORDER BY sort')
print(c.fetchone())
print(c.fetchone())

c.execute('SELECT * FROM book WHERE book.category = 1')
print(c.fetchall())

for row in c.execute('SELECT name, price FROM book ORDER BY sort'):
    print(row)


