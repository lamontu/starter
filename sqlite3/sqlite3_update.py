# -*- coding: utf-8 -*-

import sqlite3


conn = sqlite3.connect('test_for_update.db')
c = conn.cursor()


c.execute('UPDATE book SET price = ? WHERE id = ?', (1000, 1))

c.execute('DELETE FROM book WHERE id = 2')

conn.commit()
conn.close()


