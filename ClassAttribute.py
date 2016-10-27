# -*- coding: utf-8 -*-

class Me(object):
    def test(self):
        print('Hello!')

def new_test():
    print('New Hello!')

me = Me()

print("hex(id(me)) >>>>")
print(hex(id(me)))

print("hex(id(me.test)) >>>>")
print(hex(id(me.test)))

print("hex(id(new_test)) >>>>")
print(hex(id(new_test)))


print("hasattr(me, 'test') >>>>")
print(hasattr(me, 'test'))

print("getattr(me, 'test') >>>>")
print(getattr(me, 'test'))


print("setattr(me, 'test') >>>>")
print(setattr(me, 'test', new_test))


print("getattr(me, 'test') >>>>")
print(getattr(me, 'test'))


print("delattr(me, 'test') >>>>")
print(delattr(me, 'test'))

print("getattr(me, 'test') >>>>")
print(getattr(me, 'test'))

print("hex(id(me.test)) >>>>")
print(hex(id(me.test)))
