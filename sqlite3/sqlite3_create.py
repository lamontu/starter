# -*- coding: utf-8 -*-

import sqlite3


conn = sqlite3.connect('test.db')

c = conn.cursor()


c.execute('''CREATE TABLE category (
             id INT PRIMARY KEY, sort INT, name TEXT)
          ''')

c.execute('''CREATE TABLE book (
             id INT PRIMARY KEY, sort INT, name TEXT, price REAL,
             category INT, FOREIGN KEY (category) REFERENCES category(id))
          ''')

conn.commit()

conn.close()


