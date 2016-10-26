# -*- coding: utf-8 -*-

class from_obj(object):
    def __init__(self, to_obj):
        self.to_obj = to_obj

print('b = [1, 2, 3]')
b = [1, 2, 3]

print('a = from_obj(b)')
a = from_obj(b)

print('id(b) >>>>')
print(hex(id(b)))
print()

print('id(a) >>>>')
print(hex(id(a)))
print()

print('id(a.to_obj) >>>>')
print(hex(id(a.to_obj)))
