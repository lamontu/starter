# -*- coding:utf-8 -*-

class Descriptor(object):
    def __get__(self, obj, type=None):
        return 'get', self, obj, type
    def __set__(self, obj, val):
        print('set', self, obj, val)
    def __delete__(self, obj):
        print('delete', self, obj)

class T(object):
    d = Descriptor()

t = T()

print('t.d:\n', t.d)
print('T.d:\n', T.d)
print()

print("t.d = 'hello':")
t.d = 'hello'
print('t.d:\n', t.d)
print('T.d:\n', T.d)

print("T.d == 'hello':")
T.d = 'hello'
print('t.d:\n', t.d)
print('T.d:\n', T.d)

