# -*- coding: utf-8 -*-
passline = 60
def func(val):
    print('Hexadecimal address of val: %x' % id(val)) 
    if val >= passline:
        print('pass')
    else:
        print('faled')
    def in_func(): # in_func obtained an attribute: a tuple (val,)
        print(val)
    in_func()
    return in_func

print('f = func(89) >>>>')
f = func(89)
print()

print('f:', f)
print('id(f): %x' % id(f))
print()


#Variable val is stored as an attribute __closure__ of function f(). 
print('f.__closure__:', f.__closure__) 
print()

print('f() >>>>')
#Function f() search parameter val in its attributes rather than in the context.
f()
