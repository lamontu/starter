# -*- coding: utf-8 -*-

def deco(func):
    def in_deco():
        print('in deco')
        func()
    print('call deco')
    return in_deco

@deco
def bar():
    print('in bar')

print()
print('type(bar) <<<<')
print(type(bar))

print()
print('bar() <<<<')
bar()
