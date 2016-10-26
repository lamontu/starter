# -*- coding: utf-8 -*-

def deco(func):
    def in_deco(x, y):
        print('in deco')
        func(x, y)
    print('call deco')
    return in_deco

#Function bar was decorated, adding other parts in the function in_deco
@deco 
def bar(x, y):
    print('in bar', x + y)

print()
print('type(bar) <<<<')
print(type(bar))

print()
print('bar() <<<<')
bar(1, 2)
